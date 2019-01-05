# Generated by Django 2.1.3 on 2018-11-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_common', '0002_auto_20181119_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='emoji',
            name='order',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='emoji',
            name='image',
            field=models.ImageField(unique=True, upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='emoji',
            name='keyword',
            field=models.CharField(max_length=16, unique=True, verbose_name='keyword'),
        ),
    ]