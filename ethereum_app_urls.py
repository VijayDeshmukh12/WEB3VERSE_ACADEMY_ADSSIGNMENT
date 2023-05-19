from django.urls import path
from balance import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fetch_balance/', views.fetch_balance, name='fetch_balance'),
]
