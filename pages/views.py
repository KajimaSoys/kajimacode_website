from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import permission_classes

@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class NavbarViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about Navbar depending on the language
    """
    serializer_class = PagesNavbarSerializer
    queryset = Navbar.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class FooterViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about Footer depending on the language
    """
    serializer_class = PagesFooterSerializer
    queryset = Footer.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class CookieElementViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about CookieElement depending on the language
    """
    serializer_class = PagesCookieElementSerializer
    queryset = CookieElement.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class MainPageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about MainPage depending on the language
    """
    serializer_class = PagesMainPageSerializer
    queryset = MainPage.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ProjectsPageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about ProjectsPage depending on the language
    """
    serializer_class = PagesProjectsPageSerializer
    queryset = ProjectsPage.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class SkillsPageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about SkillsPage depending on the language
    """
    serializer_class = PagesSkillsPageSerializer
    queryset = SkillsPage.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class AboutPageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about AboutPage depending on the language
    """
    serializer_class = PagesAboutPageSerializer
    queryset = AboutPage.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class TermsPageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about TermsPage depending on the language
    """
    serializer_class = PagesTermsPageSerializer
    queryset = TermsPage.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class PrivacyPageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about PrivacyPage depending on the language
    """
    serializer_class = PagesPrivacyPageSerializer
    queryset = PrivacyPage.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class CookiesPageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that returns information about CookiesPage depending on the language
    """
    serializer_class = PagesCookiesPageSerializer
    queryset = CookiesPage.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        return queryset