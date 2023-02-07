from django.db import models


class Group(models.Model):
    """
    Описание модели Group приложения Core
    """
    class Meta:
        verbose_name = 'Группа работ'
        verbose_name_plural = 'Группы работ'

    id = models.BigAutoField(verbose_name='Идентификатор', primary_key=True)
    name =  models.CharField(verbose_name='Название группы', max_length=100)

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
    name = models.CharField(verbose_name='Название группы', max_length=250)
    description = models.TextField(verbose_name='Описание', max_length=5000, blank=True)
    link = models.URLField(verbose_name='Ссылка на проект', blank=True)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name