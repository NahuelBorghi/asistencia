from django.db import models
from .Components_copy.student import Student
from .Components_copy.course import Course
from .Components_copy.attendanceManager import attendanceMgr
# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    class Meta:
        app_label='myapp'
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    # setters
    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    
    def set_surname(self, surname):
        self.surname = surname
    
    # getters
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname