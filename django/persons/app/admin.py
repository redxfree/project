from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'city', 'gender']
    list_filter = ['gender']
    search_fields = ['name']
    

admin.site.register(Person, PersonAdmin)
