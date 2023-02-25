from django.contrib import admin
from .models import *
from django.http import HttpResponse
from django.urls import re_path as url

@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    def save_image(self, request, *args, **kwargs):
        image = ProjectImages.objects.filter(id=kwargs['id']).values('image')[0]['image']
        file_path = 'media/' + image

        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(),
                                        content_type='image/jpeg')
                response['Content-Disposition'] = 'inline; filename=' + '.jpeg'
                return response

    def get_urls(self):
        urls = super(ProjectImagesAdmin, self).get_urls()
        custom_urls = [
            url(
                r'^(?P<id>.+)/save_image/$',
                self.admin_site.admin_view(self.save_image),
                name='save_image',
            ),
        ]
        return custom_urls + urls


class ProjectImagesInline(admin.StackedInline):
    model = ProjectImages
    fields = ('image', 'main', 'alt', 'image_tag', )
    readonly_fields = ('image_tag', )
    extra = 0


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'get_group', 'isActive')
    inlines = (ProjectImagesInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
        # if request.user.is_superuser:
        #     return qs
        # else:
        #     return qs.filter(personal=False)


    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.personal and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj=obj)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass