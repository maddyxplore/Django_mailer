from django.urls import path

from . import views

urlpatterns = [
    path('mailer', views.mailer, name='mailer'),
    path('mail',views.mail, name='mail'),
]

