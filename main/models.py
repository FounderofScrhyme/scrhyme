from accounts.models import CustomUser
from django.db import models
from django.db.models.deletion import CASCADE
from .validators import validate_is_audio
from django.utils import timezone


beat = (('All I want is you', 'All I want is you'), ('smoke', 'Smoke'))


class Songs(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='user', on_delete=models.CASCADE)
    username = models.CharField(verbose_name='Artist Name', max_length=30)
    songtitle = models.CharField(verbose_name='Song Title', max_length=30)
    beat = models.TextField(choices=beat)
    song = models.FileField(upload_to='uploaded_songs', validators=[validate_is_audio])
    lyrics = models.TextField(verbose_name='lyrics', max_length=1400)
    created_at = models.DateTimeField(verbose_name='posted at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.username


class Vocals(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='user', on_delete=models.CASCADE)
    username = models.CharField(verbose_name='Artist Name', max_length=30)
    vocal = models.FileField(upload_to='uploaded_vocals', validators=[validate_is_audio])
    request = models.TextField(verbose_name='request', max_length=256)
    created_at = models.DateTimeField(verbose_name='posted at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)
