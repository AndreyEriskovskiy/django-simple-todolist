# Generated by Django 4.2.7 on 2024-02-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options_alter_task_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='term',
        ),
        migrations.AddField(
            model_name='task',
            name='datetime_joined',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время добавления'),
        ),
    ]
