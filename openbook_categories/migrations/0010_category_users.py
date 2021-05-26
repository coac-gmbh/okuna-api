# Generated by Django 2.2.16 on 2021-05-26 00:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openbook_categories', '0009_auto_20190909_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
