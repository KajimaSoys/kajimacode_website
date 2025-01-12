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
from core import views as core_views
from service import views as service_views
from pages import views as page_views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'groups', core_views.GroupViewSet)
router.register(r'works', core_views.WorkViewSet)
router.register(r'skills', core_views.SkillViewSet)
# router.register(r'projects/personal', core_views.PersonalProjectViewSet)
# router.register(r'projects/team', core_views.TeamProjectViewSet)
router.register(r'projects', core_views.ProjectViewSet)
router.register(r'pages/navbar', page_views.NavbarViewSet)
router.register(r'pages/footer', page_views.FooterViewSet)
router.register(r'pages/cookie-element', page_views.CookieElementViewSet)
router.register(r'pages/rate', page_views.RateElementViewSet)
router.register(r'pages/main', page_views.MainPageViewSet)
router.register(r'pages/projects', page_views.ProjectsPageViewSet)
router.register(r'pages/skills', page_views.SkillsPageViewSet)
router.register(r'pages/about', page_views.AboutPageViewSet)
router.register(r'pages/terms', page_views.TermsPageViewSet)
router.register(r'pages/privacy', page_views.PrivacyPageViewSet)
router.register(r'pages/cookies', page_views.CookiesPageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/get_ascii_part_<int:key>', core_views.get_ascii, name='get_ascii'),
    path('api/v1/send_request', service_views.OrderCreateView.as_view()),
    path('api/v1/send_rate', service_views.RateCreateView.as_view()),
    path('api/v1/send_feedback', service_views.FeedbackCreateView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
