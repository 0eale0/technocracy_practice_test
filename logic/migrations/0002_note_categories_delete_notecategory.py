# Generated by Django 4.0.5 on 2022-06-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='categories',
            field=models.ManyToManyField(to='logic.category'),
        ),
        migrations.DeleteModel(
            name='NoteCategory',
        ),
    ]
