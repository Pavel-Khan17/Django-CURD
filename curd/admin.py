from django.contrib import admin
from .models import studentModel, departmentModel
# Register your models here.

@admin.register(studentModel)
class studentModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'email']


@admin.register(departmentModel)
class departmentModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']