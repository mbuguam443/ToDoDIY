from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import datetime
# Create your views here.


def Hompage(request):
    return render(request,'index.html')

def SubmitForm(request):
    obj=Todo()
    obj.title=request.POST.get('Title')
    obj.description=request.POST.get('Description')
    obj.priority=request.POST.get('Priority')
    obj.save()
    
    mydict={
      "alltodos":Todo.objects.all()
    }
    return render(request,'todolist.html',context=mydict)

def TodoList(request):
    mydict={
      "alltodos":Todo.objects.all()
    }
    return render(request,'todolist.html',context=mydict)


def TodoDelete(request,id):
    obj=Todo(id)
    obj.delete()
    mydict={
      "alltodos":Todo.objects.all()
    }
    return render(request,'todolist.html',context=mydict)


def TodoSearch(request):
    q=request.GET.get('q')
    
    mydict={
      "alltodos":Todo.objects.filter(title__contains=q)
    }
    return render(request,'todolist.html',context=mydict)     

def TodoEdit(request,id):
    obj=Todo.objects.get(id=id)
    
    mydict={
      "title":obj.title,
      "description":obj.description,
      "priority":obj.priority,
      "id":obj.id
    }
    return render(request,'edit.html',context=mydict)


def TodoUpdate(request):

    obj=Todo.objects.get(id=request.POST.get('id'))
    obj.title=request.POST.get('Title')
    obj.description=request.POST.get('Description')
    obj.priority=request.POST.get('Priority')
    obj.created_at=datetime.datetime.now()
    obj.save()
    
    mydict={
      "alltodos":Todo.objects.all()
    }
    return render(request,'todolist.html',context=mydict)