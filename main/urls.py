from django.urls import path
from .views import DysonAPI, DysonDetailView


urlpatterns = [
    path('first_page', DysonAPI.as_view()),
    path('first_page/<int:pk>', DysonDetailView.as_view()),
    ]
