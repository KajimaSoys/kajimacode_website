from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('name', 'mail', 'message', 'project_version', 'created', 'screen_resolution', 'browser_language',)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    model = Rate
    list_display = ('source', 'rate_value', 'project_version', 'created', 'screen_resolution', 'browser_language',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ('source', 'rate_message', 'project_version', 'created', 'screen_resolution', 'browser_language',)
