from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from django.contrib import messages
# Create your views here.

def index(request):
    formulario_clientes = PostForm()
    if request.method == 'POST':
        formulario_clientes = PostForm(request.POST)
        if formulario_clientes.is_valid():
            formulario_clientes.save()
            messages.success(request, 'Datos guardados')
            
            return redirect('portal/index.html')
            
    return render(request, 'portal/index.html', {'formulario_clientes': formulario_clientes})
