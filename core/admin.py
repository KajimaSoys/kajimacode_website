from django.contrib import admin
from django.http import HttpResponse
from django.urls import re_path as url
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin, SortableAdminBase
import os
from core.models import (
    Group,
    Project,
    ProjectImages,
    Work,
    Skill
)
from core.forms import ProjectForm, SkillForm


@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ('project', 'thumbnail', 'alt')
    list_editable = ('alt', )
    list_filter = ('project', )
    ordering = ('project__order', 'order')

    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}"><img src="{obj.image.url}" width="500" /></a>')
        return "Предпросмотр пока недоступен. Добавьте фото и сохраните категорию для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']

    def save_image(self, request, *args, **kwargs):
        image = ProjectImages.objects.filter(id=kwargs["id"]).values("image")[0]["image"]
        file_path = "media/" + image

        if os.path.exists(file_path):
            with open(file_path, "rb") as fh:
                response = HttpResponse(fh.read(),
                                        content_type="image/jpeg")
                response["Content-Disposition"] = "inline; filename=" + ".jpeg"
                return response

    def get_urls(self):
        urls = super(ProjectImagesAdmin, self).get_urls()
        custom_urls = [
            url(
                r"^(?P<id>.+)/save_image/$",
                self.admin_site.admin_view(self.save_image),
                name="save_image",
            ),
        ]
        return custom_urls + urls


class ProjectImagesInline(SortableInlineAdminMixin, admin.StackedInline):
    model = ProjectImages
    fields = ("image", "main", "alt", "image_tag",)
    readonly_fields = ("image_tag",)
    extra = 0


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    class Media:
        js = ("//ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js",
              "//unpkg.com/dropzone@5/dist/min/dropzone.min.js",
              "js/common/dropzone_setup.js",
              "js/common/fieldsets_title_setup.js",)
        css = {
            "all": ("//unpkg.com/dropzone@5/dist/min/dropzone.min.css", "css/custom_dropzone.css")
        }
    list_display = ("order", "name_ru", "get_group", "isActive")
    filter_horizontal = ("group",)
    list_filter = ("group", "isActive", "personal",)
    fieldsets = [
        (None, {
            "fields": [
                ("name_ru", "name"),

            ],
        }),
        (_("title Описание"), {
            "fields": [
                ("description_short_ru", "description_short"),
                ("description_ru", "description")
            ],
        }),
        (_("title Список групп"), {
            "fields": [
                "group"
            ],
        }),

        (_("title Мета информация"), {
            "classes": ("collapse",),
            "fields": [
                "link",
                "git",
                "personal",
                "isActive"
            ],
        })
    ]
    search_fields = ("name", "name_ru", "group__name")
    search_help_text = "Поиск доступен по полям: Название проекта (рус.), Название проекта (англ.), Группа"
    inlines = (ProjectImagesInline,)
    form = ProjectForm

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.personal and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj=obj)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    class Media:
        js = ("//ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js",
              "js/common/fieldsets_title_setup.js",)

    list_display = ("order", "name_ru", "skill_type", "isActive")
    list_filter = ("skill_type", "isActive")
    fieldsets = [
        (None, {
            "fields": [
                ("skill_type", "isActive"),
                ("name_ru", "name"),

            ],
        }),
        (_("title Описание"), {
            "fields": [
                ("description_ru", "description")
            ],
        }),
    ]
    search_fields = ("name", "name_ru")
    search_help_text = "Навык (рус.), Навык (англ.)"
    form = SkillForm
