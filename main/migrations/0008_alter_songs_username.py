# Generated by Django 4.2.7 on 2023-12-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_songs_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='username',
            field=models.CharField(max_length=30, verbose_name='username'),
        ),
    ]
