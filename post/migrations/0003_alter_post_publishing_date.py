# Generated by Django 4.0 on 2021-12-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_content_alter_post_publishing_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publishing_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi'),
        ),
    ]
