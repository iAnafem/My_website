# Generated by Django 2.2.3 on 2019-07-05 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190705_1546'),
        ('accounts', '0003_auto_20190705_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment'),
        ),
    ]
