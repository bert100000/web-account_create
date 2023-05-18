from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Todo 
from .forms import TodoForm 
from datetime import datetime
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def completed_by_id(request,id):
    todo=Todo.objects.get(id=id)
    todo.completed=not todo.completed
    todo.date_completed=datetime.now() if todo.completed else None
    todo.save()
    
    return redirect('todo')

@login_required
def delete(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo')

@login_required
def completed(request):
    todos=Todo.objects.filter(user=request.user,completed=True)
    return render(request,'./todo/completed.html',{'todos':todos})

@login_required
def create_todo(request):
    message=''
    form=TodoForm()
    
    try:
        if request.method=='POST':
            print(request.POST)
            if request.user.is_authenticated:
                form = TodoForm(request.POST)
                todo=form.save(commit=False)
                todo.user=request.user
                todo.date_completed=datetime.now() if todo.completed else None
                todo.save()
        
                return redirect('todo')
    except Exception as e:
        print(e)
        message='資料輸入錯誤' 
         
    return render(request,'./todo/createtodo.html',{'form':form,'message':message})



def todo(request):
    todos=None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    print(todos)
    
    
    return render(request, './todo/todo.html',{'todos':todos})

@login_required
def viewtodo(request,id):
    try:
        todo = Todo.objects.get(id=id)
        
        if request.method=='GET':
            form=TodoForm(instance=todo)
        
        elif request.method=="POST":
            if request.POST.get('update'):
                
                form=TodoForm(request.POST,instance=todo)
                if form.is_valid():
                #資料暫存
                    todo=form.save(commit=False)
                
                    todo.date_completed=datetime.now() if todo.completed else None
                    form.save()
            elif request.POST.get('delete'):
                todo.delete()
                return redirect('todo')
                
        return render(request,'./todo/viewtodo.html',{'todo':todo,'form':form})
    except Exception as e:
            print(e)
    return render(request,'./todo/404.html')
    '''if todo.completed:
            todo.date_completed=datetime.now()
                
      else:
                    todo.date_completed=None'''
                
        # todo = get_object_or_404(Todo,id=id)
        # #print(todo)
        
    
    