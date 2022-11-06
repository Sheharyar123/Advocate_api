from django.contrib import admin
from .models import Advocate, Company

# Register your models here.


class AdvocateAdmin(admin.ModelAdmin):
    list_display = ("username", "company", "twitter")


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")


admin.site.register(Advocate, AdvocateAdmin)
admin.site.register(Company, CompanyAdmin)
