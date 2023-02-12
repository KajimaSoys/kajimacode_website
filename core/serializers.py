from rest_framework import serializers
from .models import *


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class CoreGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name', )


# class CoreProjectSerializer(serializers.HyperlinkedModelSerializer):
#     group = CoreGroupSerializer()
#     class Meta:
#         model = Project
#         fields = ('group', 'name', 'name_ru', 'description', 'description_ru',  'link', 'git',)


class CoreImageSerializer(serializers.ModelSerializer):
    # project = CoreProjectSerializer()

    class Meta:
        model = ProjectImages
        fields = ('main', 'image')#'__all__'#('image', 'main', 'project')


class ProjectGroupSerializer(serializers.ModelSerializer):
    """Предположительно ProjectGroupSerializer"""
    image_set = serializers.SerializerMethodField()
    group = CoreGroupSerializer()

    def get_image_set(self, obj):
        queryset = ProjectImages.objects.filter(project=obj).prefetch_related().order_by('-main')
        serializer = CoreImageSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = Project
        fields = ('id', 'name', 'name_ru', 'description', 'description_ru', 'image_set', 'link', 'git', 'group')


class CoreWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = ('name', 'description', 'link')


