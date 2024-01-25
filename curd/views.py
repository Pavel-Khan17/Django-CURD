from django.shortcuts import render, redirect, get_object_or_404
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



# update operation 
""" updating the student info """
def updateStudent(request,pk):
  student = get_object_or_404(studentModel, id=pk)
  if request.method == 'POST':
    form = studentModelForm(request.POST, request.FILES, instance=student)
    if form.is_valid():
      form.save()
      return redirect("home")
  else: 
    form = studentModelForm(instance=student)
  context = {'form' : form}
  return render(request, "add_student.html", context)  