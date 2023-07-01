from django.urls import path
from .views import DysonAPI


urlpatterns = [
    path('first_page', DysonAPI.as_view())
]