# Generated by Django 2.2.3 on 2019-07-09 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_comment_last_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_on',
        ),
    ]
