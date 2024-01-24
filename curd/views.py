from django.shortcuts import render, redirect
from .models import studentModel
from .forms import studentModelForm
# Create your views here.


#  Read operation 
"""showing all the student list """
def home(request):
  students = studentModel.objects.all()
  context={'students' : students}
  return render(request, "home.html", context)



# create operation 
""" adding the student """
def addStudent(request):
  form = studentModelForm()
  if request.method == 'POST':
    form = studentModelForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form': form}
  return render(request,"add_student.html", context)