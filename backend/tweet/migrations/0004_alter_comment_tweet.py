# Generated by Django 3.2.16 on 2023-07-09 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_auto_20230708_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tweet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tweet.tweet'),
            preserve_default=False,
        ),
    ]