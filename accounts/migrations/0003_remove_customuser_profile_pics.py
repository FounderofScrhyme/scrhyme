# Generated by Django 4.2.7 on 2023-12-16 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_image',
        ),
    ]
