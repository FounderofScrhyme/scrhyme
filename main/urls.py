from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('terms/', views.ShowTermsView.as_view(), name="terms"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('songs/', views.SongsFeedView.as_view(), name="songs_feed"),
    path('songs-detail/<int:pk>/', views.SongsDetailView.as_view(), name="songs_detail"),
    path('beat-download/', views.BeatDownloadView.as_view(), name="beat_download"),
    path('songs-post/', views.SongsPostView.as_view(), name="songs_post"),
    path('songs-update/<int:pk>/', views.SongsUpdateView.as_view(), name="songs_update"),
    path('songs-delete/<int:pk>/', views.SongsDeleteView.as_view(), name="songs_delete"),
    path('request-vocal-processing/', views.RequestVocalProcessingView.as_view(), name="request"),
]
