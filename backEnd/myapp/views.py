from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Student, Course, Attendance
from .forms import StudentForm, CourseForm
from datetime import datetime
# Create your views here.

# Función para renderizar la página principal
def home(request):
    return render(request, 'base.html')

# Función para listar todos los estudiantes
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Función para agregar un nuevo estudiante
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de estudiantes
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, "student_add.html", {'form': form})

# Función para editar un estudiante existente
def student_edit(request, student_id):
    # Obtenemos el estudiante con el id especificado en la URL
    # si modifico el id no edita sino que crea un nuevo estudiante. deberia darle un numero internamente en vez de manejar todo por el atributo id
    student = get_object_or_404(Student, id=student_id)
    courses = Course.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # Redirigir a la página de estudiantes
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    context = {
        'courses': courses,
        'form': form,
        'student_id': student_id,
    }
    return render(request, 'student_edit.html', context)

# Función para eliminar un estudiante existente
def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    # Redirigir a la página de estudiantes
    return redirect('student_list')

# Función para listar todos los cursos
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            # redirigir a la página de cursos
            return redirect('course_list')
    else:
        form = CourseForm()
    # Si la solicitud no es una solicitud POST, muestra el formulario vacío
    return render(request,"course_add.html",{'form':form})

def course_edit(request, course_id):
    # obtiene el curso correspondiente al id o muestra un error 404 si no existe
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            # redirigir a la página de cursos
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    context = {
        'form': form,
        'course_id': course_id,
    }
    # muestra el formulario con el curso actual como instancia del formulario
    return render(request, 'course_edit.html', context)

def course_delete(request, course_id):
    # obtiene el curso correspondiente al id o muestra un error 404 si no existe
    course = Course.objects.get(id=course_id)
    course.delete()
    # redirige a la lista de cursos
    return redirect('course_list')

def attendance_by_course(request, course_id):
    # uso get para traer un curso especifico
    # filtra las asistencias correspondientes al curso
    # usa select_related para traer los datos de la tabla student y usarlos bajo el mismo nombre
    course = Course.objects.get(id=course_id)
    attendances = Attendance.objects.filter(course_id=course_id).select_related('student')
    context = {
        'attendances': attendances,
        'course': course}
    # muestra la lista de asistencias
    return render(request, 'attendance_by_course.html', context)

def mark_attendance(request):
    if request.method == 'POST':
        # obtiene los ids del estudiante y el curso desde la solicitud
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        # obtiene la fecha actual
        date = datetime.today().strftime('%Y-%m-%d')
        # crea un nuevo objeto de asistencia y lo guarda
        attendance = Attendance(student_id=student_id, course_id=course_id, date=date, present=True)
        attendance.save()
        # devuelve una respuesta JSON exitosa
        return JsonResponse({'success': True})
    else:
        # devuelve una respuesta JSON de error si la solicitud no es una solicitud POST
        return JsonResponse({'success': False})