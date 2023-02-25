from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import permission_classes


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Groups to be viewed
    """
    queryset = Group.objects.all()
    serializer_class = CoreGroupSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class PersonalProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Personal Projects
    """
    queryset = Project.objects.filter(isActive=True, personal=True)
    serializer_class = ProjectSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class TeamProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Team Project
    """
    queryset = Project.objects.filter(isActive=True)
    serializer_class = ProjectSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for All Project
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


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
