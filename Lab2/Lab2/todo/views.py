from django.shortcuts import render, HttpResponse, redirect, reverse
from pprint import pprint

# Create your views here.

class Task:
    def __init__(self,t_id,t_title,t_priority,t_done=False):
        self.id=t_id
        self.title=t_title
        self.priority=t_priority
        self.done=t_done
todo = [
    {'id': 1, 'title': 'study', 'priority': 1, 'done': False},
    {'id': 2, 'title': 'study', 'priority': 1, 'done': True},
    {'id': 3, 'title': 'study', 'priority': 1, 'done': False},
    {'id': 4, 'title': 'study', 'priority': 1, 'done': False},
    {'id': 5, 'title': 'study', 'priority': 1, 'done': True},
]


def home(request):

    return render(request, 'todo/home.html', context={'todos': todo})


def detail(request, **kwargs):
    task_id = kwargs['id']
    task = get_task_by_id(task_id)
    return render(request,'todo/task_detail.html',context={'task':task})


def done(request, **kwargs):
    task_id = kwargs['id']
    task = get_task_by_id(task_id)
    task['done'] = True
    return redirect(reverse('todo:home'))


def delete(request, **kwargs):
    task_id = kwargs['id']
    task = get_task_by_id(task_id)
    todo.remove(task)
    print(task)
    return redirect(reverse('todo:home'))


def get_task_by_id(task_id):
    task = list(filter(lambda task: task['id'] == task_id, todo))[0]
    return task


def add_task(request):
    # print(request['post'])
    t_id=int(request.POST['id'])
    t_title=request.POST['title']
    t_priority=request.POST['prio']
    task = Task(t_id,t_title,t_priority)
    todo.append(task.__dict__)
    pprint (todo)
    return redirect(reverse('todo:home'))
