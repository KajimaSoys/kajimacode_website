from django.contrib import admin
from .models import *

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass