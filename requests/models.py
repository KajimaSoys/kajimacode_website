from django.db import models


class Order(models.Model):
    """
    Описание модели Order приложения Requests
    """

    name = models.CharField(verbose_name='Имя', max_length=150)
    mail = models.CharField(verbose_name='Email', max_length=150)
    message = models.TextField(verbose_name='Сообщение', blank=True)

    project_version = models.CharField(verbose_name='Версия приложения', blank=True, max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    user_agent = models.CharField(verbose_name='UserAgent', blank=True, max_length=2000)
    screen_resolution = models.CharField(verbose_name='Разрешение экрана', blank=True, max_length=100)
    browser_language = models.CharField(verbose_name='Язык браузера', blank=True, max_length=100)
    timezone = models.CharField(verbose_name='Временная зона', blank=True, max_length=100)
    cookie = models.TextField(verbose_name='Cookie', blank=True, max_length=5000)

    def __str__(self):
        return f'{self.name} - {self.mail} - {self.created}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Rate(models.Model):
    """
    Описание модели Rate приложения Requests
    """

    source_choices = (
        ('about', 'About page'),
        ('cookie', 'Cookie page'),
        ('main', 'Main page'),
        ('privacy', 'Privacy page'),
        ('projects', 'Projects page'),
        ('skills', 'Skills page'),
        ('soloproj', 'Solo project page'),
        ('terms', 'Terms page'),
    )

    source = models.CharField(verbose_name='Источник оценки', max_length=20, choices=source_choices)

    rate_value = models.IntegerField(verbose_name='Оценка', blank=True)

    project_version = models.CharField(verbose_name='Версия приложения', max_length=10)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    user_agent = models.CharField(verbose_name='UserAgent', blank=True, max_length=2000)
    screen_resolution = models.CharField(verbose_name='Разрешение экрана', blank=True, max_length=100)
    browser_language = models.CharField(verbose_name='Язык браузера', blank=True, max_length=100)
    timezone = models.CharField(verbose_name='Временная зона', blank=True, max_length=100)

    def __str__(self):
        return f'{self.source} - {self.rate_value} - {self.created}'

    class Meta:
        verbose_name = 'Оценка раздела'
        verbose_name_plural = 'Оценки разделов'


class Feedback(models.Model):
    """
    Описание модели Feedback приложения Requests
    """

    source_choices = (
        ('about', 'About page'),
        ('cookie', 'Cookie page'),
        ('main', 'Main page'),
        ('privacy', 'Privacy page'),
        ('projects', 'Projects page'),
        ('skills', 'Skills page'),
        ('soloproj', 'Solo project page'),
        ('terms', 'Terms page'),
    )

    source = models.CharField(verbose_name='Источник оценки', max_length=20, choices=source_choices)

    rate_message = models.CharField(verbose_name='Сообщение', blank=True, max_length=500)

    project_version = models.CharField(verbose_name='Версия приложения', max_length=10)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    user_agent = models.CharField(verbose_name='UserAgent', blank=True, max_length=2000)
    screen_resolution = models.CharField(verbose_name='Разрешение экрана', blank=True, max_length=100)
    browser_language = models.CharField(verbose_name='Язык браузера', blank=True, max_length=100)
    timezone = models.CharField(verbose_name='Временная зона', blank=True, max_length=100)

    def __str__(self):
        return f'{self.source} - {self.created}'

    class Meta:
        verbose_name = 'Отзыв о качестве'
        verbose_name_plural = 'Отзывы о качестве'
