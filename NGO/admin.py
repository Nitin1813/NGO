from django.contrib import admin
from .models import Donate, DonateDetail


# Register your models here.

admin.site.register(Donate)
admin.site.register(DonateDetail)