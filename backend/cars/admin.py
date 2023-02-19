from django.contrib import admin
from .models import Car

class carAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'photo', 'url', 'year', 'user_id')
# Register your models here.
admin.site.register(Car, carAdmin)
