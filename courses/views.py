from django.shortcuts import render, redirect
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import Course, Group
from .forms import GroupForm
from students.models import Student, Payment

@login_required(login_url='login')
def all_courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses_table.html', context)
@login_required(login_url='login')
def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        Course.objects.create(
            name=course_name
        )
        return redirect('courses')
    context = {
        'item': 'Kurs'
    }
    return render(request, 'form-templete.html', context)


@login_required(login_url='login')
def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('courses')

    context = {
        'item': course,
        'orqaga': 'courses'
    }
    return render(request, 'delete-item.html', context)




@login_required(login_url='login')
def all_groups(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }

    return render(request, 'groups_table.html', context)

@login_required(login_url='login')
def add_group(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():

            group = form.save(commit=False)
            group.complete = False
            group.save()
            return redirect('groups')


    context = {
        'form': form,
        'item': 'Group'
    }
    return render(request, 'form-templete.html', context)
@login_required(login_url='login')
def group_deatail(request, pk):
    group = Group.objects.get(id=pk)
    students = group.student_set.all()
    new_students = Student.objects.filter(course=group.course, group=None)

    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        if start_date:
            y, m, d = map(int, str(start_date).split('-'))
            group.start = date(y, m, d)
            group.finish = date(y, m, d) + relativedelta(months=group.continuity)
            group.save()


    payments = group.payment_set.filter(complete=False)

    payment_list = []
    for i in range(1, group.continuity+1):
        month = []
        for payment in payments:
            if payment.month == str(i):
                month.append(payment)
        if len(students) != 0:
            pount = 100 / len(students) * (len(students) - len(month))
            payment_list.append(
                (i, month, pount)
            )



    context = {
        'group': group,
        'students': len(students),
        'new_students': new_students,
        'payments':payments,
        "payment_list": payment_list

    }
    return render(request, 'group-detail.html', context)
@login_required(login_url='login')
def end_group(request, pk):
    group = Group.objects.get(id=pk)
    group.finish = date.today()
    group.save()
    return redirect('group_detail', pk=pk)
@login_required(login_url='login')
def complete_group(request, pk):
    group = Group.objects.get(id=pk)
    payments = group.payment_set.filter(complete=False)
    students = group.student_set.all()
    print(len(payments))
    if len(payments) == 0:
        group.complete = True
        group.finish = date.today()
        group.save()
        for student in students:
            student.finish = True
            student.save()
    else:
        messages.info(request, 'Tolovlar toliq qilinmagan')
    return redirect('group_detail', pk=pk)

@login_required(login_url='login')
def add_student_to_group(request, student_pk, group_pk):
    group = Group.objects.get(id=group_pk)
    student = Student.objects.get(id=student_pk)

    student.group = group
    student.save()

    for i in range(1, group.continuity+1):
        Payment.objects.create(
            student=student,
            group=group,
            amount=group.amount,
            month=i,
            comment='',
            complete=False
        )


    return redirect('group_detail', pk=group.id)
@login_required(login_url='login')
def delete_group(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        payments = Payment.objects.filter(group=group, complete=False)
        for  payment in payments:
            payment.delete()
        group.delete()
        return redirect('groups')
    context = {
        'item': group,
        'orqaga': 'groups'
    }
    return render(request, 'delete-item.html', context)