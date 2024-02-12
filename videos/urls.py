from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", views.HomeView.as_view(), name = "home"),
    path("video/<int:pk>/", views.MovieView.as_view(), name = "movie")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)