from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import studentModel, departmentModel
from .forms import studentModelForm
# Create your views here.

#  Read operation and search operation 
"""showing all the student list """
def home(request):
  if request.method == 'GET':
    q = request.GET.get('q')
    if q == 'M':
      students = studentModel.objects.filter(gender='M')
    elif q == 'F':
      students = studentModel.objects.filter(gender='F')
    elif q is not None:
      students = studentModel.objects.filter(
        Q(name__icontains=q)|
        Q(email__icontains=q)|
        Q(department_name__name__icontains=q)|
        Q(gender__exact=q)
      )
      print(students)
    else:
      students = studentModel.objects.all().order_by('-created_date')
  context={'students' : students}
  return render(request, "home.html", context)



# create operation 
""" adding the student """
def addStudent(request):
  form = studentModelForm()
  departments = departmentModel.objects.all()
  if request.method == 'POST':
    form = studentModelForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form': form, 'departments': departments}
  return render(request,"add_student.html", context)



# update operation 
""" updating the student info """
def updateStudent(request,pk):
  student = studentModel.objects.get(id=pk) 
  departments = departmentModel.objects.all()
  if request.method == 'POST':
    form = studentModelForm(request.POST, request.FILES, instance=student)
    if form.is_valid():
      form.save()
      return redirect("home")
  else: 
    form = studentModelForm(instance=student)
  context = {'form' : form, 'departments': departments}
  return render(request, "add_student.html", context)  



# delete operation 
""" delete the student info from database """
def deleteStudent(request,pk):
  student = get_object_or_404(studentModel, id=pk)
  if request.method == 'POST':
    student.delete()
    return redirect('home')
  context={'student': student}
  return render(request, "delete.html", context)