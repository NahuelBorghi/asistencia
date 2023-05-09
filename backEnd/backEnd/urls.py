"""
URL configuration for backEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import student_list, student_add, student_edit, student_delete, course_add, course_delete, course_edit, course_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', student_list, name='student_list'),
    path('student_add/', student_add),
    path('student_edit/<int:student_id>', student_edit, name='student_edit'),
    path('student_delete/<int:student_id>/', student_delete, name='student_delete'),
    path('courses/', course_list, name='course_list'),
    path('course_add/', course_add),
    path('course_edit/<int:course_id>', course_edit, name='course_edit'),
    path('course_delete/<int:course_id>/', course_delete, name='course_delete'),
]
