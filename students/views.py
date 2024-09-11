import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from PIL import Image, ImageDraw, ImageFont
import io

from .models import Student, Payment, StudentCertificate
from .forms import SudentForm, PaymentForm


@login_required(login_url='login')
def all_students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student_table.html', context)


@login_required(login_url='login')
def add_student(request):
    form = SudentForm()
    if request.method == 'POST':
        form = SudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.finish = False
            student.save()

            return redirect('all_students')
    context = {
        'form': form,
        'item': 'Student'
    }
    return render(request, 'form-templete.html', context)


@login_required(login_url='login')
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':

        payments = Payment.objects.filter(student=student)
        for payment in payments:
            payment.delete()

        student.delete()
        return redirect('all_students')
    context = {
        'item': student,
        'orqaga': 'students'
    }
    return render(request, 'delete-item.html', context)


@login_required(login_url='login')
def editStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = SudentForm(instance=student)
    if request.method == 'POST':
        form = SudentForm(data=request.POST, files=request.FILES, instance=student)
        if form.is_valid():
            stud = form.save(commit=False)

            stud.save()
            return redirect('student_profile', pk=student.id)
    context = {
        'item': student,
        'form': form
    }
    return render(request, 'form-templete.html', context)


@login_required(login_url='login')
def students_payments(request):
    payments = Payment.objects.filter(complete=False)
    context = {
        'payments': payments
    }
    return render(request, 'payments_table.html', context)


@login_required(login_url='login')
def student_profile(request, pk):
    student = Student.objects.get(id=pk)
    groups = student.group
    context = {
        'student': student,
        'groups': groups
    }
    return render(request, 'student-profile.html', context)


@login_required(login_url='login')
def pay_for_student(request, pk):
    payment = Payment.objects.get(id=pk)
    month = payment.month
    student = payment.student.name
    form = PaymentForm(instance=payment)
    if request.method == 'POST':
        form = PaymentForm(instance=payment, data=request.POST, files=request.FILES)
        if form.is_valid():
            pay = form.save(commit=False)
            if pay.amount >= payment.group.amount:
                pay.complete = True
                pay.save()
            else:
                pay.amount = int(payment.group.amount) - int(pay.amount)
                pay.complete = False
                pay.save()
        return redirect('payments')
    context = {
        'form': form,
        'student': student,
        'month': month,
        'payment': payment.group.amount
    }

    return render(request, 'form-payment.html', context)


@login_required(login_url='login')
def generate_certificate(request, pk):
    student = Student.objects.get(id=pk)
    course = student.course
    year = datetime.date.today().year
    try:
        student_name = student.name.split()
        if len(student_name) > 1:
            student_name = f"{student_name[0]} {student_name[1]}"
        else:
            student_name = f"{student_name[0]}"
        img = Image.open('static/assets/images/certificate.png')
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("static/Roboto-Regular.ttf", 210)
        idfont = ImageFont.truetype("static/Roboto-Regular.ttf", 110)
        coursefont = ImageFont.truetype("static/Roboto-Regular.ttf", 110)
        d.text((150, 1000), f"{student_name}", fill=(0, 0, 0), font=font)
        d.text((2550, 2000), f"{year}-{student.id}", fill=(0, 0, 0), font=idfont)
        d.text((150, 1450), f'"{course.name}" course', fill=(110, 170, 36), font=idfont)

        # Сохраняем изображение в объект BytesIO
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        # Предположим, что buffer - это объект StringIO, содержащий PNG-данные
        # Создаем объект PIL Image из данных StringIO
        img1 = Image.open(buffer)

        # Сохраняем изображение в файл

        img1.save(f"static/certificates/{student_name}{student.id}{course.name}.png", format="PNG")
        try:
            student_ = StudentCertificate.objects.get(student=student)
        except:
            student_ = None
        if not student_:
            StudentCertificate.objects.create(
                name=f'{student.name}{student.id}{course.name}',
                student=student,
                image=f"certificates/{student.name}{student.id}{course.name}.png",
                course=student.course
            )
        # Отправляем изображение в ответе
        return HttpResponse(buffer.getvalue(), content_type="image/png")
    except:
        student_ = StudentCertificate.objects.get(student=student)
        buffer = io.BytesIO()
        buffer.seek(0)
        # Предположим, что buffer - это объект StringIO, содержащий PNG-данные
        # Создаем объект PIL Image из данных StringIO
        img1 = Image.open(f"static/assets/images/certificates/{student.name}{student.id}{course.name}.png")
        img1 = Image.open(buffer)
        student_name = student.name.split()
        if len(student_name) > 1:
            student_name = f"{student_name[0]} {student_name[1]}"
        else:
            student_name = f"{student_name[0]}"
        # Сохраняем изображение в файл
        return HttpResponse(buffer.getvalue(), content_type="image/png")
