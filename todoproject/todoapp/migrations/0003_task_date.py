# Generated by Django 4.2.3 on 2023-07-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_task1_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-12-12'),
            preserve_default=False,
        ),
    ]