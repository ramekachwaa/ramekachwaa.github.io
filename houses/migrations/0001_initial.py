# Generated by Django 3.2.14 on 2022-07-20 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('skype', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Balcony', 'Balcony'), ('Cable TV', 'Cable TV'), ('Internet', 'Internet'), ('Tennis Courts', 'Tennis Courts'), ('Parking', 'Parking')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images')),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images')),
                ('address', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('sale', 'sale'), ('rent', 'rent')], max_length=100)),
                ('area', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.agent')),
                ('amenities', models.ManyToManyField(to='houses.Amenity')),
            ],
        ),
        migrations.CreateModel(
            name='Image_of_house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_imgs', to='houses.house')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='houses.blog')),
            ],
        ),
    ]
