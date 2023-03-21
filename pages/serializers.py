from rest_framework import serializers
from pages.models import *


class PagesNavbarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Navbar
        fields = ('projects_link',
                  'skills_link',
                  'about_link',
                  'telegram_button')


class PagesFooterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Footer
        fields = ('overview_link',
                  'projects_link',
                  'skills_link',
                  'about_link',
                  'terms_link',
                  'privacy_link',
                  'cookies_link')


class PagesCookieElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CookieElement
        fields = ('element_text',
                  'link',
                  'button')


class PagesRateElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RateElement
        fields = ('rate_title',
                  'rate_title_success',
                  'feedback_title',
                  'feedback_description',
                  'feedback_message_label',
                  'feedback_message_placeholder',
                  'feedback_success_message',
                  'feedback_error_message',
                  'send_button',
                  'send_button_wait',
                  'retry_button',)


class PagesMainPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainPage
        fields = ('language',
                  'contact_button',
                  'projects_button',
                  'get_started_button',
                  'learn_more_button',
                  'send_message_button',
                  'send_message_button_wait',
                  'retry_button',
                  'main_title',
                  'introduce_title',
                  'introduce_description',
                  'project_title',
                  'project_description',
                  'stages_title',
                  'discussion_title',
                  'discussion_description',
                  'concept_title',
                  'concept_description',
                  'server_dev_title',
                  'server_dev_description',
                  'ui_dev_title',
                  'ui_dev_description',
                  'test_title',
                  'test_description',
                  'deploy_title',
                  'deploy_description',
                  'first_string',
                  'second_string',
                  'third_string',
                  'technologies_title',
                  'django_title',
                  'django_description',
                  'postgresql_title',
                  'postgresql_description',
                  'vue_title',
                  'vue_description',
                  'contact_pretitle',
                  'contact_title',
                  'contact_description',
                  'name_label',
                  'name_placeholder',
                  'email_label',
                  'email_placeholder',
                  'message_label',
                  'message_placeholder',
                  'privacy_text',
                  'privacy_link',
                  'success_message',
                  'error_message',
                  'review_title',
                  'review_description',
                  'first_text',
                  'first_author',
                  'first_post',
                  'second_text',
                  'second_author',
                  'second_post',
                  'third_text',
                  'third_author',
                  'third_post',)


class PagesProjectsPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectsPage
        fields = ('back_button',)


class PagesSkillsPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillsPage
        fields = ('title',
                  'backend_title',
                  'backend_description',
                  'frontend_title',
                  'frontend_description',
                  'other_title',
                  'other_description',)


class PagesAboutPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutPage
        fields = ('title',
                  'about_text',
                  'resume_text',
                  'download_button',)


class PagesTermsPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TermsPage
        fields = ('language',
                  'data')


class PagesPrivacyPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrivacyPage
        fields = ('language',
                  'data')


class PagesCookiesPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CookiesPage
        fields = ('language',
                  'data')


