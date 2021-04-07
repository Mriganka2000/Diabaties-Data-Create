from django.contrib import admin
from .models import UserData, OriginalData

# Register your models here.
admin.site.register(UserData)
admin.site.register(OriginalData)