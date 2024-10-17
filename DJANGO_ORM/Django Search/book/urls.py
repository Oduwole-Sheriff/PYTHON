from django.urls import path
from book import views

urlpatterns = [
    path('', views.post_search, name="poat_search")
]