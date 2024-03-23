
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-message/', views.send_message, name='send-message'),
    path('portfolio/<int:id>/', views.portfolio, name='portfolio'),
]

