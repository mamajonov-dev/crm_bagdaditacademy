# Generated by Django 4.2 on 2024-09-10 06:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('student_time', models.CharField(blank=True, choices=[('8:00 - 10:00', '8:00 - 10:00'), ('10:00 - 12:00', '10:00 - 12:00'), ('12:00 - 14:00', '12:00 - 14:00'), ('14:00 - 16:00', '14:00 - 16:00'), ('16:00 - 18:00', '16:00 - 18:00')], max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.IntegerField(blank=True, default=998, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('finish', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.group')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCertificate',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='certificates/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('month', models.CharField(blank=True, max_length=100, null=True)),
                ('sale', models.IntegerField(blank=True, default=0, null=True)),
                ('payment_check', models.ImageField(blank=True, default=None, null=True, upload_to='payment_cheks/')),
                ('comment', models.TextField(blank=True, null=True)),
                ('complete', models.BooleanField(blank=True, default=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.group')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
            options={
                'ordering': ['month'],
            },
        ),
    ]
