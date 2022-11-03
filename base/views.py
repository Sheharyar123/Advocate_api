from rest_framework import generics

from .models import Advocate
from .serializers import AdvocateSerializer


class AdvocateList(generics.ListAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer




