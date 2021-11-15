from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)
