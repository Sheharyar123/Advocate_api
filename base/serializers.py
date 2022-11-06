from rest_framework import serializers
from .models import Advocate, Company


class AdvocateSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source="company.name")

    class Meta:
        model = Advocate
        fields = ["id", "username", "bio", "company", "twitter", "profile_pic"]


class CompanySerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = ["id", "name", "bio", "logo", "employee_count"]

    def get_employee_count(self, obj):
        return obj.advocate_set.count()
