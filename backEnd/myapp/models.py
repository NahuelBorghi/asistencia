from django.db import models
# creacion de los models que se usan para la migracion automatica a la base de datos.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    class Meta:
        app_label='myapp'
    def __str__(self):
        return f"{self.name} {self.surname}"

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        app_label='myapp'
    def __str__(self):
        return f"{self.name}"

class Attendance(models.Model):
    id = models.IntegerField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

class Matriculation(models.Model):
    id = models.IntegerField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id')
    on_going = models.BooleanField(default=False)
    course_approved = models.BooleanField(default=False)
    final_approved = models.BooleanField(default=False)
    class Meta:
        app_label='myapp'