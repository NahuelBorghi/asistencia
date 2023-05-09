from django import forms
from myapp.models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name','surname']

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['id','name']

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']