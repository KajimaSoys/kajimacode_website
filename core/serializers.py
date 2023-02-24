from rest_framework import serializers
from core.models import *


class CoreGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name', )


class CoreImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = ('main', 'image', 'alt')


class ProjectGroupSerializer(serializers.ModelSerializer):
    image_set = serializers.SerializerMethodField()
    # group = Project.get_group(self)

    def get_image_set(self, obj):
        queryset = ProjectImages.objects.filter(project=obj).prefetch_related().order_by('-main')
        serializer = CoreImageSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = Project
        fields = ('id',
                  'name',
                  'name_ru',
                  'description',
                  'description_ru',
                  'description_short',
                  'description_short_ru',
                  'image_set',
                  'link',
                  'git',
                  'get_group')


class CoreWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = ('name', 'description', 'link')


