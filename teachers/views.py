
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required(login_url='login')
def all_teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teachers-table.html', context)

@login_required(login_url='login')
def teacher_profile(request, pk):
    teacher = Teacher.objects.get(id=pk)
    groups = teacher.group_set.all()
    all_students = 0
    summa = 0
    for group in groups:
        all_students += group.all_students()
        for student in group.student_set.filter(finish=False):
            summa += group.amount * 1
    context = {
        'teacher': teacher,
        'summa': int(summa / 100 * 50),
        'all_students': all_students
    }
    return render(request, 'teacher-profile.html', context)

@login_required(login_url='login')
def add_teacher(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        Teacher.objects.create(
            name=course_name
        )
        return redirect('all_teachers')
    return render(request, 'add-teacher.html')
@login_required(login_url='login')
def edit_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(instance=teacher, files=request.FILES, data=request.POST)
        if form.is_valid():
            teach = form.save(commit=False)
            teach.save()
            return redirect('teacher_profile', pk=teacher.id)
    context = {
        'form': form,
        'item': 'Teacher'
    }
    return render(request, 'form-templete.html', context=context)