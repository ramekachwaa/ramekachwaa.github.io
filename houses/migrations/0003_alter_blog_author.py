# Generated by Django 3.2.14 on 2022-07-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_alter_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
