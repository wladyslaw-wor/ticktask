# Generated by Django 4.1.7 on 2023-03-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_todo_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecomplited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
