from django.shortcuts import render, redirect
from .models import ToDo
from .forms import Form
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):

    if request.method == 'POST':
        form = Form(request.POST or None)
    
        if form.is_valid():
            form.save()
            items = ToDo.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'home.html', {'items': items})
    else:
        items = ToDo.objects.all
        return render(request, 'home.html', {'items': items})

def about(request):
    return render(request, 'about.html', {})

def delete(request, list_id):
    one_item = ToDo.objects.get(pk=list_id)
    one_item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')

def check_off(request, list_id):
    one_item = ToDo.objects.get(pk=list_id)
    one_item.completed = True
    one_item.save()
    return redirect('home')

def check_on(request, list_id):
    one_item = ToDo.objects.get(pk=list_id)
    one_item.completed = False
    one_item.save()
    return redirect('home')

def edit(request, list_id):
    
    if request.method == 'POST':
        item = ToDo.objects.get(pk=list_id)

        form = Form(request.POST or None, instance=item)
    
        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
    else:
        item = ToDo.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})    