from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='matches-home'),
    path('refresh/', views.refresh, name='matches-refresh'),
]
