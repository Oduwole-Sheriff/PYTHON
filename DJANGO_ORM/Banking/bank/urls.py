from django.urls import path
from bank import views

urlpatterns = [
    path('', views.process_payment, name='payment')
]