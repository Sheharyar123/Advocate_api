from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("advocates/", views.AdvocateList.as_view(), name="advocate_list"),
    path("advocate/<int:pk>/", views.AdvocateDetail.as_view(), name="advocate_detail"),
    path("companies/", views.CompanyList.as_view(), name="company_list"),
    path("company/<int:pk>/", views.CompanyDetail.as_view(), name="company_detail"),
]