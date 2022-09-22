from django.core import validators 
from django.core.validators import * 

from django import forms
from django.forms import ModelForm
from projectApp.models import employee, uniq
import re

regex1 = r'\b[A-Za-z0-9._%+-]+@gmail.com\b'
regex2 = r'\b[A-Za-z0-9._%+-]+@outlook.com\b'
regex3 = r'\b[A-Za-z0-9._%+-]+@ymail.com\b'

def emp_email(email):
    if(re.fullmatch(regex1, email)):
        pass
    elif(re.fullmatch(regex2, email)):
        pass 
    elif(re.fullmatch(regex3, email)):
        pass  
    else:
        raise forms.ValidationError('email is not valid')

def p_num(val):
    if (len(str(val)))==10:
        pass
    else:
        raise forms.ValidationError("phone number should 10 digit")
    


CHOICES =[('Male','Male'),('Female','Female')]
hobbies_choices = (('reading','reading'),('writing','writing'),('music','music'))
class UniqForm(ModelForm):
    username = forms.CharField(validators = [validators.MaxLengthValidator(10)])
    email = forms.EmailField(validators = [emp_email])
    address = forms.CharField(max_length=100)
    phone_no = forms.IntegerField(validators=[p_num])
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    hobbies = forms.MultipleChoiceField(choices=hobbies_choices, widget  = forms.CheckboxSelectMultiple)
    department = forms.ChoiceField(choices=[('IT','IT'),('Marketing','Marketing'),('account','account')])   


          
    
    class Meta:
        model =  uniq
        fields = "__all__"


# class StudentForm(ModelForm):
#     class Meta:
#         model = employee
#         fields = "__all__"

# class Student(ModelForm):
#     class Meta:
#         firlds = "__all__"
        

