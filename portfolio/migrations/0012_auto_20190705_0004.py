# Generated by Django 2.2.3 on 2019-07-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20190704_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
