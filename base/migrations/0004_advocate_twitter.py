# Generated by Django 4.1.3 on 2022-11-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_advocate_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='twitter',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
