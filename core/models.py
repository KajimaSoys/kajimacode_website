from django.db import models
import os
from django.utils.html import mark_safe

class Group(models.Model):
    """
    Описание модели Group приложения Core
    """
    class Meta:
        verbose_name = 'Группа работ'
        verbose_name_plural = 'Группы работ'

    id = models.BigAutoField(verbose_name='Идентификатор', primary_key=True)
    name = models.CharField(verbose_name='Название группы', max_length=100)


    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Описание модели Project приложения Core
    """
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    id = models.BigAutoField(verbose_name='Идентификатор', primary_key=True)
    group = models.ForeignKey(verbose_name='Группа', to=Group, on_delete=models.CASCADE)

    name = models.CharField(verbose_name='Название проекта (англ.)', max_length=250)
    name_ru = models.CharField(verbose_name='Название проекта (рус.)', max_length=250)
    description = models.TextField(verbose_name='Описание (англ.)', max_length=5000, blank=True)
    description_ru = models.TextField(verbose_name='Описание (рус.)', max_length=5000, blank=True)

    # TODO create full and short description
    # TODO create get_absolute_url method, to allow route to the project page

    link = models.URLField(verbose_name='Ссылка на проект', blank=True)
    git = models.URLField(verbose_name='Ссылка на гит', blank=True)

    path = models.CharField(verbose_name='Папка проекта', blank=True, max_length=200)
    isActive = models.BooleanField(verbose_name='Активен?', default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            super(Project, self).save(*args, **kwargs)
            path = f'project_{str(self.id)}'
            try:
                os.mkdir(f'media/projects/{path}')
            except FileExistsError:
                pass
            self.path = f'projects/{path}'
        super(Project, self).save(*args, **kwargs)


class ProjectImages(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    main = models.BooleanField(verbose_name='Главное изображение?', default=False)
    # TODO create alt field

    def get_upload_path(self, filename):
        path = Project.objects.get(id=self.project_id).path
        return f'media/{path}/{filename}'

    image = models.ImageField(verbose_name='Изображение проекта', blank=True, upload_to=get_upload_path, max_length=500)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.path)
        super().delete()


    def image_tag(self):
        if self.pk is None:
            image = '<p>Предпросмотр пока не доступен, загрузите изображение и сохраните проект</p>'
        else:
            image = f'<a href="/media/{self.image}">' \
                    f'<img src="/media/{self.image}" width="600" height="337" />' \
                    '</a>'
        return mark_safe(image)
    image_tag.short_description = 'Предпросмотр'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return str(self.image).replace('projects/', '')



class Work(models.Model):
    """
    Описание модели Work приложения Core
    """
    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    id = models.BigAutoField(verbose_name='Идентификатор', primary_key=True)
    name = models.CharField(verbose_name='Название работы', max_length=250)
    description = models.TextField(verbose_name='Описание', max_length=5000, blank=True)
    link = models.URLField(verbose_name='Ссылка на компанию, где работа', blank=True)
    isActive = models.BooleanField(verbose_name='Активен?', default=True)

    def __str__(self):
        return self.name