# Generated by Django 2.2.3 on 2019-07-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_project_full_description_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='full_description',
            field=models.TextField(blank=True, default='', max_length=2500),
        ),
    ]
