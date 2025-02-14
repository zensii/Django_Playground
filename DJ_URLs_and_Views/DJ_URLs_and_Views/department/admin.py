from django.contrib import admin

from DJ_URLs_and_Views.department.models import Department


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass