# Generated by Django 2.2.5 on 2019-12-09 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0032_auto_20191209_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitynotificationssubscription',
            old_name='new_posts_notifications_enabled',
            new_name='new_post_notifications',
        ),
    ]