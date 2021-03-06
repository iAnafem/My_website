# Generated by Django 2.2.2 on 2019-07-01 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('homepage', '0020_delete_myflatpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewFlatpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='description', max_length=200)),
                ('text_block', models.CharField(help_text='text_block', max_length=200)),
                ('flatpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flatpages.FlatPage')),
            ],
            options={
                'verbose_name': 'Содержание страницы',
                'verbose_name_plural': 'Содержание страницы',
            },
        ),
    ]
