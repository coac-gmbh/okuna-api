# Generated by Django 2.2.16 on 2021-12-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0039_auto_20211027_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='group_type',
            field=models.CharField(choices=[('C', 'City'), ('Q', 'Company'), ('I', 'Institution'), ('U', 'Research'), ('P', 'Project'), ('E', 'Event')], default='I', max_length=1),
            preserve_default=False,
        ),
    ]