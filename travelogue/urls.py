from django.urls import path
from . import views

app_name = 'travelogue'

# just 2 pages for showing travelogue models atributes


urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
