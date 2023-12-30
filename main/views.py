import logging
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContactForm, SongsPostForm, RequestVocalProcessingForm

from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from .models import Songs

logger = logging.getLogger(__name__)


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        songs = get_object_or_404(Songs, pk=self.kwargs['pk'])
        return self.request.user == songs.user


class IndexView(TemplateView):
    template_name = "index.html"


class ShowTermsView(TemplateView):
    template_name = "terms.html"


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "contact.html"

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Your message has been sent.')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class SongsFeedView(ListView):
    model = Songs
    template_name = 'songs_feed.html'
    paginate_by = 5

    def get_queryset(self):
        tunes = Songs.objects.order_by('-created_at')
        return tunes


class SongsDetailView(DetailView):
    model = Songs
    template_name = 'songs_detail.html'


class BeatDownloadView(TemplateView):
    template_name = 'beat_download.html'


class SongsPostView(LoginRequiredMixin, CreateView):
    model = Songs
    template_name = 'songs_post.html'
    form_class = SongsPostForm
    success_url = reverse_lazy('main:songs_feed')

    def form_valid(self, form):
        songs = form.save(commit=False)
        songs.user = self.request.user
        songs.save()
        messages.success(self.request, 'Your song has been posted.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to post the song.")
        return super().form_invalid(form)


class SongsUpdateView(LoginRequiredMixin, OnlyYouMixin, UpdateView):
    model = Songs
    template_name = 'songs_update.html'
    form_class = SongsPostForm

    def get_success_url(self):
        return reverse_lazy('main:songs_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'Your songs has been updated.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update the song.")
        return super().form_invalid(form)


class SongsDeleteView(LoginRequiredMixin, OnlyYouMixin, DeleteView):
    model = Songs
    template_name = 'songs_delete.html'
    success_url = reverse_lazy('main:songs_feed')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "The post has been deleted.")
        return super().delete(request, *args, **kwargs)


class RequestVocalProcessingView(LoginRequiredMixin, TemplateView):
    template_name = 'request_vocal_processing.html'
    success_url = reverse_lazy('main:songs_feed')
