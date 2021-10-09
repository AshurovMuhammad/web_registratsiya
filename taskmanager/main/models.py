from django.db import models


class Task(models.Model):
    title = models.CharField('Sarlavha', max_length=50)
    task = models.TextField('Tavsif')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Vazifa'
        verbose_name_plural = 'Vazifalar'

