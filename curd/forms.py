from django import forms
from django.core.exceptions import ValidationError
from .models import studentModel ,departmentModel


class studentModelForm(forms.ModelForm):
  name = forms.CharField(max_length=50, required=False)
  email = forms.EmailField( max_length=50 ,error_messages={'unique': "this email is already taken."})

  class Meta:
    model = studentModel
    fields = '__all__'
    
  def clean_name(self): 
    return self.cleaned_data['name'].capitalize() 

  def __init__(self, *args, **kwargs):
    super(studentModelForm, self).__init__(*args, **kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'peer h-full w-full rounded-md border border-blue-gray-200 border-t-transparent !border-t-blue-gray-200 bg-transparent px-3 py-3 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:!border-t-gray-900 focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50'
