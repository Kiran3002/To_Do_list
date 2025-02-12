from django.shortcuts import render,redirect
from .models import Task,Contactus
from datetime import datetime
# Create your views here.
def index(request):
    all_tasks=Task.objects.filter(is_active=True).order_by('completed')
    context={
        'tasks': all_tasks
    }
    return render(request, 'todo/index.html',context)

def add_task(request):
    if request.method=="POST":
        title = request.POST['title']
        description = request.POST['description']
        image= request.FILES['task-image']
        print(title,description)
        task=Task(title=title,description=description, image=image)
        task.save()
        return redirect('home')
    else:
        return render(request, 'todo/new_task.html')

def delete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.is_active=False
    task.save()
    return redirect('home')

def complete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.completed=True
    task.completed_at= datetime.now()
    task.save()
    return redirect('home')


def update_task(request,task_id):
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        task=Task.objects.get(id=task_id)
        task.title=title
        task.description=description
        task.save()
        return redirect('home')
    else:
        task=Task.objects.get(id=task_id)
        context = {
            'task' : task 
        }
    return render(request,'todo/update_task.html',context)

def contact_us(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        description=request.POST['description']
        contact=Contactus(name=name,email=email,phone=phone,description=description)
        contact.save()
        return redirect('contact')
    else:
        return render(request,'contact/new_contact.html')
