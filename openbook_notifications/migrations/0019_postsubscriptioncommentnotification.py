# Generated by Django 2.2.5 on 2020-02-27 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0070_auto_20200226_1514'),
        ('openbook_notifications', '0018_auto_20200226_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostSubscriptionCommentNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openbook_posts.PostComment')),
            ],
        ),
    ]
