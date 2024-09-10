from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='logout'),
    path('login/', login_user, name='login'),
    path('admin-profile/', admin_dashboard, name='admin_profile'),
    path('add-expenses/', addexpenses, name='add_expenses'),
]
