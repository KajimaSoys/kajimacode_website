"""kajimasoys_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views as coreViews
from requests.views import OrderCreateView
from pages import views as pageViews
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'groups', coreViews.GroupViewSet)
router.register(r'works', coreViews.WorkViewSet)
router.register(r'projects/personal', coreViews.PersonalProjectViewSet)
router.register(r'projects/team', coreViews.TeamProjectViewSet)
router.register(r'projects', coreViews.ProjectViewSet)
router.register(r'pages/navbar', pageViews.NavbarViewSet)
router.register(r'pages/footer', pageViews.FooterViewSet)
router.register(r'pages/cookie-element', pageViews.CookieElementViewSet)
router.register(r'pages/main', pageViews.MainPageViewSet)
router.register(r'pages/projects', pageViews.ProjectsPageViewSet)
router.register(r'pages/skills', pageViews.SkillsPageViewSet)
router.register(r'pages/about', pageViews.AboutPageViewSet)
router.register(r'pages/terms', pageViews.TermsPageViewSet)
router.register(r'pages/privacy', pageViews.PrivacyPageViewSet)
router.register(r'pages/cookies', pageViews.CookiesPageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/get_ascii', coreViews.get_ascii),
    path('api/v1/send_request', OrderCreateView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
