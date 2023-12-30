# Generated by Django 4.2.7 on 2023-12-04 09:07

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
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('songtitle', models.CharField(max_length=30, verbose_name='songtitle')),
                ('beat', models.TextField(choices=[('All I want is you', 'All I want is you'), ('smoke', 'Smoke')])),
                ('song', models.FileField(default='', upload_to='songs/')),
                ('lyrics', models.TextField(max_length=1400, verbose_name='lyrics')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='posted at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'Songs',
            },
        ),
    ]
