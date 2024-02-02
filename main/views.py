from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Task


def to_do_list(request: HttpRequest):
    
    if request.method == 'POST':
        task = request.POST.get('task', None)
        task_id = request.POST.get('delete_one', None)
        delete_all_Tasks = request.POST.get('delete_all', None)
        
        if task:
            Task.objects.create(description=task)
            
        if task_id:
            Task.objects.filter(id=task_id).delete()
            
        if delete_all_Tasks:
            tasks = Task.objects.all()
            tasks.delete()
            
    
        return redirect('main')
            
    
    
    else:
        all_tasks = Task.objects.all().order_by('-datetime_joined').order_by('-datetime_updated')
        

    
        return render(request, 'index.html', context={'tasks': all_tasks})


def edit_list(request: HttpRequest, task_id=False):
    if request.method == 'POST':
        if task_id:
            updated_task = request.POST.get('task_description')
            task = Task.objects.get(id=task_id)
            task.description = updated_task
            task.save()
            all_tasks = Task.objects.all().order_by('-datetime_joined').order_by('-datetime_updated')
            
        return render(request, 'index.html', context={'tasks': all_tasks})
            
        
    else:
        if task_id:
            task = Task.objects.filter(id=task_id)
            return render(request, 'edit.html', {'task': task})
        