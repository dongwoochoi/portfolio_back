# Generated by Django 5.2.1 on 2025-05-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_post_author_remove_post_title_post_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.CharField(max_length=100),
        ),
    ]
