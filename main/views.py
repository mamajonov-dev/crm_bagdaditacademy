from django.shortcuts import render, redirect
from courses.models import Group, Course
from teachers.models import Teacher
from .models import Expenses
from students.models import Student
from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .form import *


@login_required(login_url='login')
def dashboard(request):
    courses = Course.objects.all()
    groups = Group.objects.all()
    teachers = Teacher.objects.all()
    expenses = Expenses.objects.all()
    new_students = Student.objects.filter(group=None)
    all_students = Student.objects.all()

    expenses_now = None
    now = date.today().month
    for date_e in expenses:
        a = int(str(date_e.month).split('-')[1])
        print(a, '============================')
        if a == now:
            expenses_now = date_e
    if expenses_now:
        oylik = expenses_now.salary() / 2
        daromad = expenses_now.salary() - expenses_now.rent - expenses_now.others - expenses_now.energy - oylik
    else:
        oylik = None
        daromad = None

    context = {
        'courses': len(courses),
        'groups': len(groups),
        'teachers': len(teachers),
        'new_students': new_students,
        'all_students': len(all_students)
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
def admin_dashboard(request):
    if request.user.username == 'mamajonov.dev':
        courses = Course.objects.all()
        groups = Group.objects.all()
        teachers = Teacher.objects.all()
        expenses = Expenses.objects.all()
        new_students = Student.objects.filter(group=None)
        all_students = Student.objects.all()
        expenses_now = None
        now = date.today().month
        for date_e in expenses:
            a = int(str(date_e.month).split('-')[1])
            print(a, '============================')
            if a == now:
                expenses_now = date_e
        if expenses_now:
            oylik = expenses_now.salary() / 2
            daromad = expenses_now.salary() - expenses_now.rent - expenses_now.others - expenses_now.energy - oylik
        else:
            oylik = None
            daromad = None

        context = {
            "expenses_now": expenses_now,
            'oylik': oylik,
            'daromad': daromad,
            'teachers': teachers,
            'all_students': len(all_students)

        }
        return render(request, 'admin-profile.html', context)

    else:
        return redirect('dashboard')


def user_register(request):
    form = User_Register_Form()
    if request.method == 'POST':
        form = User_Register_Form(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            pass
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('login')

    return render(request, 'auth-login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def addexpenses(request):
    form = ExpensesForm()
    if request.method == 'POST':
        form = ExpensesForm(request.POST, request.FILES)
        if form.is_valid():
            expenses = form.save(commit=False)
            expenses.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'item': 'Chiqim'
    }
    return render(request, 'form-templete.html', context=context)
