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
    task_list=Task.objects.all()
    return render(request,'testapp/about.html',{'task_list':task_list})
def delete_view(request,id):
    task=Task.objects.get(id = id)
    task.delete()
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
 