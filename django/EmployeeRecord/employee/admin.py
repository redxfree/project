from django.contrib import admin
from .models import *



# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
      list_display = [ '__str__','age',  'gender','salary','designation','department','contact','user']
      
      
admin.site.register(Employee, EmployeeAdmin)

admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Material)
admin.site.register(Attendance)
admin.site.register(Transport)
admin.site.register(AvailableMaterial)

admin.site.register(Apprasial)
admin.site.register(ApprasialStep)
admin.site.register(ApprasialResult)

admin.site.register(OverTime)
admin.site.register(Leave)


