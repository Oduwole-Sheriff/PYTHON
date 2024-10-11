from django.urls import path, include
from Base.views import LoginAPI, ResgisterAPI, PersonView

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('register/', ResgisterAPI.as_view()),
    path('person/', PersonView.as_view()),
]