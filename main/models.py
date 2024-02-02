from django.db import models

class Task(models.Model):

    description = models.TextField(blank=True, verbose_name='Описание задачи')
    datetime_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')
    datetime_updated = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')

    class Meta:
        db_table = 'Task'
        verbose_name = "Задачу"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.description

    

