from django.urls import path
from . import views

app_name = 'note'

# just two page for showing Notes models atributes

urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
