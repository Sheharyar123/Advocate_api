from django.contrib import admin
from .models import Advocate, Company
# Register your models here.

class AdvocateAdmin(admin.ModelAdmin):
    list_display = ("username", "company", "bio")

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")


admin.site.register(Advocate, AdvocateAdmin)
admin.site.register(Company, CompanyAdmin)