from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    logo = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "companies"
        ordering = [
            "id",
        ]

    def __str__(self):
        return self.name


class Advocate(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True
    )
    username = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    twitter = models.URLField(unique=True, null=True, blank=True)
    profile_pic = models.URLField(null=True, blank=True)

    class Meta:
        ordering = [
            "id",
        ]

    def __str__(self):
        return self.username
