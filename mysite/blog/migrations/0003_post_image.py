# Generated by Django 2.2.2 on 2019-06-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190627_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to='static/blog/img'),
        ),
    ]
