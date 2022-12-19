from django.urls import path
from . import views

app_name = 'travelogue'

urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
