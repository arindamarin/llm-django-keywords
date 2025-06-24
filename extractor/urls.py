from django.urls import path
from .views import extract_keywords

urlpatterns = [
    path("predict/", extract_keywords),
]