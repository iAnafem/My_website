# Generated by Django 2.2.2 on 2019-06-26 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20190626_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='technology',
            new_name='technologies',
        ),
    ]
