from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ClientForm
from django.contrib import messages

# Create your views here.

def createOrder(request):
    form = ClientForm()
    if request.method == 'POST':
        #print('posting:', request.POST)
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('new/')
    context = {'form':form}
    return render(request, 'portal/index.html', context)

def FormDone(request):
    return render(request, 'portal/new.html')








