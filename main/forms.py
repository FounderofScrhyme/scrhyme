import os

from django import forms
from django.core.mail import EmailMessage
from .models import Songs


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Email address')
    title = forms.CharField(label='Title', max_length=30)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name.'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your Email address.'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Enter a title.'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter your message.'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'Contact {}'.format(title)
        message = 'SenderName: {0}\nMailaddress: {1}\nMessage:\n{2}'.format(name, email, message)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()


class SongsPostForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ('username', 'songtitle', 'beat', 'song', 'lyrics')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class RequestVocalProcessingForm(forms.Form):
    name = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email address')
    vocal = forms.FileField(label='Vocal')
    request = forms.CharField(label='Request', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your Username.'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter the same email address used during the Stripe payment.'

        self.fields['vocal'].widget.attrs['class'] = 'form-control'
        self.fields['vocal'].widget.attrs['placeholder'] = 'Choose a vocal file.'

        self.fields['request'].widget.attrs['class'] = 'form-control'
        self.fields['request'].widget.attrs['placeholder'] = 'What kind of processing would you like for your vocal?' \
                                                             ' For example, "Apply T-Pain style autotune, add a wet delay, and then put a short reverb."'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        vocal = self.cleaned_data['vocal']
        request = self.cleaned_data['request']

        subject = 'Contact {}'.format(title)
        message = 'SenderName: {0}\nMailaddress: {1}\nRequest:\n{2}'.format(name, email, vocal, request)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()
