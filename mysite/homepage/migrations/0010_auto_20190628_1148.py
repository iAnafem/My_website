# Generated by Django 2.2.2 on 2019-06-28 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20190628_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='header1',
            new_name='main_header',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='header2',
            new_name='secondary_header',
        ),
    ]