from django.urls import path

from . import views

app_name = 'studb'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:textbook_id>/', views.textbook, name='textbook'),
]