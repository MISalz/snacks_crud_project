# Generated by Django 4.0.4 on 2022-05-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='Title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='snack',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
