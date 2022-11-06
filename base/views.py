from django.db.models import Q
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer


class AdvocateList(generics.ListCreateAPIView):
    # queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            try:
                return Advocate.objects.filter(
                    Q(company__name__icontains=query) | Q(username__icontains=query)
                )
            except Advocate.DoesNotExist:
                pass
        else:
            return Advocate.objects.all()


class AdvocateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer


class CompanyList(generics.ListCreateAPIView):
    # queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            try:
                return Company.objects.filter(name__icontains=query)
            except Company.DoesNotExist:
                pass
        else:
            return Company.objects.all()


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["name"] = user.name
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
