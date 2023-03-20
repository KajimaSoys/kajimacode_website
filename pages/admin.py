from django.contrib import admin
from .models import *


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    pass


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    pass


@admin.register(CookieElement)
class CookieAdmin(admin.ModelAdmin):
    pass


@admin.register(RateElement)
class RateAdmin(admin.ModelAdmin):
    pass

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('language',)
        }),
        ('Main section', {
            'fields': ('main_title',)
        }),
        ('Introduce section', {
            'fields': ('introduce_title', 'introduce_description',)
        }),
        ('Project section', {
            'fields': ('project_title', 'project_description',)
        }),
        ('Stages section', {
            'fields': (('stages_title',),
                       ('discussion_title', 'discussion_description', 'concept_title', 'concept_description',
                        'server_dev_title', 'server_dev_description', 'ui_dev_title', 'ui_dev_description',
                        'test_title', 'test_description', 'deploy_title', 'deploy_description',),
                       ('first_string', 'second_string', 'third_string',),)
        }),
        ('Technologies section', {
            'fields': (('technologies_title',),
                       ('django_title', 'django_description', 'postgresql_title', 'postgresql_description',
                        'vue_title', 'vue_description', ),)
        }),
        ('Contact section', {
            'fields': (('contact_pretitle', 'contact_title', 'contact_description',),
                       ('name_label', 'name_placeholder', 'email_label', 'email_placeholder', 'message_label',
                        'message_placeholder',),
                       ('privacy_text', 'privacy_link',),
                       ('success_message', 'error_message',),)
        }),
        ('Review section', {
            'fields': (('review_title', 'review_description',),
                       ('first_text', 'first_author', 'first_post', 'second_text', 'second_author', 'second_post',
                        'third_text', 'third_author', 'third_post',),)
        }),
        # ('Feedback section', {
        #     'fields': (('rate_title', 'rate_title_success', 'feedback_title', 'feedback_description',),
        #                ('feedback_message_label', 'feedback_message_placeholder',),
        #                ('feedback_success_message', 'feedback_error_message',),)
        # }),
        ('Buttons', {
            'fields': ('contact_button', 'projects_button', 'get_started_button', 'learn_more_button',
                       'send_message_button', 'send_message_button_wait', 'retry_button',)
        }),

    )


@admin.register(ProjectsPage)
class ProjectsPageAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillsPage)
class SkillsPageAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    pass


@admin.register(TermsPage)
class TermsPageAdmin(admin.ModelAdmin):
    pass


@admin.register(PrivacyPage)
class PrivacyPageAdmin(admin.ModelAdmin):
    pass


@admin.register(CookiesPage)
class CookiesPageAdmin(admin.ModelAdmin):
    pass

