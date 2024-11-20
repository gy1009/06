# Generated by Django 4.2.16 on 2024-11-20 19:39

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
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='书店名')),
                ('description', models.TextField(verbose_name='书店简介')),
                ('image', models.ImageField(upload_to='shop/images/', verbose_name='书店封面')),
                ('url', models.URLField(blank=True, verbose_name='书店链接')),
            ],
            options={
                'verbose_name': '书店',
                'verbose_name_plural': '书店',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('watchAgain', models.BooleanField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
