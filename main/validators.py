import os
from django.core.exceptions import ValidationError

def validate_is_audio(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in ['.wav', '.mp3', '.acc']:
        raise ValidationError('Only audio files are available.')
