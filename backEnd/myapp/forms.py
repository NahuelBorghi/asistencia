from django import forms
from myapp.models import Student

class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name','surname']