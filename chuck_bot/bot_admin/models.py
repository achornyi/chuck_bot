from django.db import models


# Create your models here.
class Greeting(models.Model):
    hello_world = models.TextField(verbose_name='Базове привітання бота')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Привітання'
        verbose_name_plural = 'Привітання'


class Helper(models.Model):
    help = models.TextField(verbose_name='Перелік можливостей бота')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Допомога'
        verbose_name_plural = 'Допомога'
