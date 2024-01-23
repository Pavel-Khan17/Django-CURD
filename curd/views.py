from django.shortcuts import render
from .models import studentModel
# Create your views here.


#  Read operation 
"""showing all the student list """
def home(request):
  students = studentModel.objects.all()
  context={'students' : students}
  return render(request, "home.html", context)