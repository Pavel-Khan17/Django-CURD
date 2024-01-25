from django.db import models
from django.utils import timezone
from .constant import GENDER_CHOICE
# Create your models here.


class departmentModel(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self) -> str:
    return self.name
  
class studentModel(models.Model):
  name            = models.CharField(max_length=50)
  email           = models.EmailField(max_length=254, unique=True)
  department_name = models.ForeignKey(departmentModel, on_delete=models.CASCADE, related_name="department")
  profile         = models.ImageField(upload_to='profile', height_field=None, width_field=None, max_length=None, blank=True)
  gender          = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True, blank=True)
  created_date    = models.DateField(auto_now_add=True)
  updated_date    = models.DateField(auto_now=True)
  def __str__(self) -> str:
    return self.name