from django.shortcuts import render


# Create your views here.

def login_register_view(request):
    return render(request, 'User/login-register.html')
