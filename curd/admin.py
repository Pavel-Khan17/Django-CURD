from django.contrib import admin
from .models import studentModel, departmentModel
# Register your models here.

@admin.register(studentModel)
class studentModelAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'email']


admin.site.register(departmentModel)