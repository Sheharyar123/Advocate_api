from rest_framework import generics

from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer


class AdvocateList(generics.ListCreateAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer


class AdvocateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer




