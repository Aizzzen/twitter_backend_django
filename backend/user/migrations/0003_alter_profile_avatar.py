# Generated by Django 3.2.16 on 2023-07-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20230710_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='Аватарка'),
        ),
    ]
