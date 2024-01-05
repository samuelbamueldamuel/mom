from django.shortcuts import render
from django.http import HttpResponse
from thing.models import Task, History
import random

# Create your views here.
def getTotal():
    completed = History.objects.filter(accepted=True).all()
    completed = list(completed)

    declined = History.objects.filter(accepted=False).all()
    declined = list(declined)
    total = 0
    for task in completed:
        total = total + task.point
    for task in declined:
        total = total - task.point

    return total

def home(request):
    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
    }
    return render(request, 'h.html', context)

def addTask(request):
    return render(request, 'addTask.html')

def recieveTask(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        point = request.POST.get('point')

    newTask = Task(name=name, point=point)
    newTask.save()

    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
    }
    return render(request, 'h.html', context)
   

def kill(request):
    Task.objects.all().delete()

    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
    }
    return render(request, 'h.html', context)
    

def choose(request, key):
    chosen = Task.objects.filter(key=key).first()

    chosen.chosen = True

    chosen.save()
    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
    }
    return render(request, 'h.html', context)
    


def toDo(request):
    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
    }
    return render(request, 'h.html', context)
    


def randomF(request):
    tasks = Task.objects.filter(chosen=True)

    tasks = list(tasks)

    length = len(tasks)

    num = random.randint(0, length)

    do = tasks[num-1]



    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
        'Rtask': do,
    }

    return render(request, 'prompt.html', context)

def accept(request, key):
    task = Task.objects.filter(key=key).first()

    new = History(name=task.name, point=task.point, accepted=True)
    new.save()

    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
    }
    return render(request, 'h.html', context)


def decline(request, key):
    task = Task.objects.filter(key=key).first()

    new = History(name=task.name, point=task.point, accepted=False)
    new.save()

    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
    }
    return render(request, 'h.html', context)

def killHistory(request):
    History.objects.all().delete()

    tasks = Task.objects.all()
    toDo = Task.objects.filter(chosen=True).all()
    history = History.objects.all()
    total = getTotal()
    context = {
        'tasks': tasks,
        'toTasks': toDo,
        'history': history,
        'total': total,
    }
    return render(request, 'h.html', context)








