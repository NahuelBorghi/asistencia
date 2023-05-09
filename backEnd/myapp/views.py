from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm
# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # redirigir a la página de estudiantes
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request,"student_add.html",{'form':form})

def student_edit(request, student_id):
    # si modifico el id no edita sino que crea un nuevo estudiante. deberia darle un numero internamente en vez de manejar todo por el atributo id
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # redirigir a la página de estudiantes
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    context = {
        'form': form,
        'student_id': student_id,
    }
    return render(request, 'student_edit.html', context)

def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_list')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            # redirigir a la página de estudiantes
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request,"course_add.html",{'form':form})

def course_edit(request, course_id):
    # si modifico el id no edita sino que crea un nuevo estudiante. deberia darle un numero internamente en vez de manejar todo por el atributo id
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            # redirigir a la página de estudiantes
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    context = {
        'form': form,
        'course_id': course_id,
    }
    return render(request, 'course_edit.html', context)

def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('course_list')