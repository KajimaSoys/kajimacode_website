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


# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class PersonalProjectViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint for Personal Projects
#     """
#     queryset = Project.objects.filter(isActive=True, personal=True)
#     serializer_class = ProjectSerializer
#
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# class TeamProjectViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint for Team Project
#     """
#     queryset = Project.objects.filter(isActive=True)
#     serializer_class = ProjectSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for All Project
    """
    queryset = Project.objects.filter(isActive=True)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = self.queryset
        personal = self.request.query_params.get('personal')
        if personal == 'True':
            queryset = queryset.filter(personal=personal)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Works to be viewed
    """
    queryset = Work.objects.all()
    serializer_class = CoreWorkSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Skills
    """
    queryset = Skill.objects.filter(isActive=True)
    serializer_class = CoreSkillSerializer


def get_ascii(request):
    with open('core/local_static/ascii_file', 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    frame = []
    sequence = []
    for i, line in enumerate(lines):
        frame.append(line.replace('\n', ''))
        if (i+1) % 99 == 0:
            sequence.append(frame)
            frame = []

    return JsonResponse({'res': sequence})
