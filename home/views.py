from django.shortcuts import render,HttpResponse,redirect
from home.models import Task

# Create your views here.
def index(request):
    context={'success': False}
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        ins=Task(title=title, description=description)
        ins.save()
        context={'success': True}
    return render(request, 'index.html' , context)
def list(request):
    alltasks = Task.objects.all()
    context={"tasks": alltasks}
    if request.method =="POST":
        nameOfTasks_list=request.POST.getlist('check_delete')
        Options_toDo=request.POST.get('Select')
        print(nameOfTasks_list)
        if Options_toDo == 'delete':
            for task in alltasks:
                if str(task) in nameOfTasks_list:
                    task.delete()
                    print("Task deleted")
            return redirect('/tasks')
        if Options_toDo=="moveStep_up":
            for task in alltasks:
                if str(task) in nameOfTasks_list:
                    task,notequal_task=notequal_task,task
                    print("Task moved Successfully")
                    break
                else:
                    notequal_task=task
            return redirect('/tasks')
    return render(request, 'list.html', context)