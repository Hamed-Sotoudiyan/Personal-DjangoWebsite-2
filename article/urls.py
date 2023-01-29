from django.urls import path
from . import views

app_name = 'article'

# one page for showing parent of article models atributes and another for details

urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
