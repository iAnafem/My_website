# Generated by Django 2.2.2 on 2019-06-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20190627_1012'),
        ('homepage', '0006_remove_homepage_civil_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='software_projects',
        ),
        migrations.AddField(
            model_name='homepage',
            name='projects',
            field=models.ManyToManyField(related_name='projects', to='portfolio.Project'),
        ),
    ]
