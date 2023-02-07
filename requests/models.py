from django.db import models

class Order(models.Model):
    """
    Описание модели Order приложения Requests
    """

    name = models.CharField(verbose_name='Имя', max_length=150)
    mail = models.CharField(verbose_name='Email', max_length=150)
    message = models.TextField(verbose_name='Сообщение', blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.mail} - {self.created}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'