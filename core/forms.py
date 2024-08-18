from django.forms import ModelForm
from core.models import Project, Skill
from django.forms import TextInput, Textarea


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
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
