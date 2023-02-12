from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import permission_classes
from django.db.models import Prefetch



@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Groups to be viewed
    """
    queryset = Group.objects.all()
    serializer_class = CoreGroupSerializer


# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class ProjectViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows Projects to be viewed
#     """
#     queryset = Project.objects.filter(isActive=True)
#     serializer_class = CoreProjectSerializer
#
#
#
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class ImagesViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows Projects to be viewed
#     """
#     queryset = ProjectImages.objects.all()
#     serializer_class = CoreImageSerializer
#
#     # def get_queryset(self):
#     #     return super().get_queryset().filter(
#     #         project_id=self.kwargs['pk']
#     #     )


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ProjectGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint for ProjectGroups
    """
    queryset = Project.objects.filter(isActive=True)
    serializer_class = ProjectGroupSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Works to be viewed
    """
    queryset = Work.objects.all()
    serializer_class = CoreWorkSerializer


def get_ascii(request):
    with open('core/local_static/ascii_raw_new', 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    frame = []
    sequence = []
    for i, line in enumerate(lines):
        frame.append(line.replace('\n', ''))
        if (i+1) % 62 == 0:
            sequence.append(frame)
            frame = []

    return JsonResponse({'res': sequence})