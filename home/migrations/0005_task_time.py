# Generated by Django 4.1.4 on 2023-01-06 15:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_task_delete_tasklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
