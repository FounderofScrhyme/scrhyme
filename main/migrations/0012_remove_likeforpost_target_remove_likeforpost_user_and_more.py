# Generated by Django 4.2.7 on 2023-12-12 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_text_comment_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likeforpost',
            name='target',
        ),
        migrations.RemoveField(
            model_name='likeforpost',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='LikeForPost',
        ),
    ]