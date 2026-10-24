from django.db import models
from django.forms import ModelForm
from core.models import Project, Skill
from django.forms import TextInput, Textarea


def https_formfield_callback(db_field, **kwargs):
    # Django 6.0 switches the URLField default scheme to https; opt in explicitly now
    if isinstance(db_field, models.URLField):
        kwargs.setdefault('assume_scheme', 'https')
    return db_field.formfield(**kwargs)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        formfield_callback = https_formfield_callback
        widgets = {
            "name_ru": TextInput(attrs={"style": "width: 90ch; box-sizing: border-box;"}),
            "name": TextInput(attrs={"style": "width: 90ch; box-sizing: border-box;"}),
            "description_short_ru": Textarea(attrs={"rows": 10, "cols": 50, "style": "width: 90ch; box-sizing: border-box;"}),
            "description_short": Textarea(attrs={"rows": 10, "cols": 50, "style": "width: 90ch; box-sizing: border-box;"}),
            "description_ru": Textarea(attrs={"rows": 10, "cols": 50, "style": "width: 90ch; box-sizing: border-box;"}),
            "description": Textarea(attrs={"rows": 10, "cols": 50, "style": "width: 90ch; box-sizing: border-box;"}),
        }


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {
            "name_ru": TextInput(attrs={"style": "width: 90ch; box-sizing: border-box;"}),
            "name": TextInput(attrs={"style": "width: 90ch; box-sizing: border-box;"}),
            "description_ru": Textarea(attrs={"rows": 10, "cols": 50, "style": "width: 90ch; box-sizing: border-box;"}),
            "description": Textarea(attrs={"rows": 10, "cols": 50, "style": "width: 90ch; box-sizing: border-box;"}),
        }
