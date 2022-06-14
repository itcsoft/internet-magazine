from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def users(request):
    return render(request, 'users.html')


