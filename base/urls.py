from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("advocates/", views.AdvocateList.as_view()),
]