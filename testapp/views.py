from django.shortcuts import render,redirect
from testapp.models import Task
from testapp.forms import TaskForm

# Create your views here.
def homeview(request):
    form = TaskForm()
    
    if request.method == 'POST':
        context={'sucess':True}
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/abt')          
    form = TaskForm()
    
    return render(request,'testapp/todoforms.html',{"form":form})


def aboutview(request):
    task_list=Task.objects.filter(deleted=False)
    return render(request,'testapp/about.html',{'task_list':task_list})



def delete_view(request,id):
    task=Task.objects.get(id = id)
    task.deleted=True
    task.save()
    return redirect('/abt')


def update_view(request,id):
    task=Task.objects.get(id = id)
    form=TaskForm(instance=task)
    if request.method == 'POST':
        form= TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/abt')
    return render(request,'testapp/update.html',{'form':form})

def search_tasks(request):
    query=request.GET['query']
    all_task= Task.objects.filter(tasktitle__icontains=query)
    task={'task_list':all_task}
    return render(request,'testapp/search_results.html',task)
    
    

def recycle(request):
    task_list=Task.objects.filter(deleted=True)
    return render(request,'testapp/recyclebin.html',{'task_list':task_list})

def restore(request,id):
    task=Task.objects.get(id=id)
    task.deleted=False
    task.save()
    return redirect('/abt')