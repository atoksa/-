from django.db import models

class ADVENTURE(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=50, default='')
    briefly = models.TextField('Краткая информация')
    book = models.FileField('Книга')
    data = models.DateTimeField('Дата добавления')
    image = models.FileField(upload_to='img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Приключения'
        verbose_name_plural = 'Приключения'