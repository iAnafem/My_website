# Generated by Django 2.2.3 on 2019-07-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_auto_20190712_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimages',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
