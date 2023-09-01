# Generated by Django 4.2.4 on 2023-09-01 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0008_mod_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mod',
            options={'ordering': ['-publish']},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ['-publish']},
        ),
        migrations.AddField(
            model_name='mod',
            name='publish',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='version',
            name='publish',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='version',
            name='slug',
            field=models.SlugField(),
        ),
    ]
