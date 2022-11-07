from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import AdminSite
from .views import *
from .models import *
from django.contrib.auth.admin import *

from blogs.models import Blog, Catergorie, Comment


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog,BlogAdmin)

class CatergorieAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('catergorie',)}

admin.site.register(Catergorie,CatergorieAdmin)
    
admin.site.register(Comment)

