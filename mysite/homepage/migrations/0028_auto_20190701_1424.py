# Generated by Django 2.2.2 on 2019-07-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0027_auto_20190701_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myflatpage',
            name='content1',
            field=models.TextField(blank=True, null=True, verbose_name='content1'),
        ),
        migrations.AlterField(
            model_name='myflatpage',
            name='content2',
            field=models.TextField(blank=True, null=True, verbose_name='content2'),
        ),
        migrations.AlterField(
            model_name='myflatpage',
            name='content3',
            field=models.TextField(blank=True, null=True, verbose_name='content3'),
        ),
        migrations.AlterField(
            model_name='myflatpage',
            name='header1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='header1'),
        ),
        migrations.AlterField(
            model_name='myflatpage',
            name='header2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='header2'),
        ),
        migrations.AlterField(
            model_name='myflatpage',
            name='text_field',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='text_field'),
        ),
    ]
