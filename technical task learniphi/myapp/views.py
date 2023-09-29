from django.shortcuts import render,redirect
from . models import Todo

# Create your views here.

def index(request):
	return render(request,'index.html')

def create(request):
	if request.method=="POST":
		Todo.objects.create(

			number=request.POST['srnumber'],
			title=request.POST['title'],
			category=request.POST['category'],
			description=request.POST['description'],
			)
		msg='create successfully'
		return render(request,'index.html',{'msg':msg})

def read(request):
	todo=Todo.objects.all()
	return render(request,'read.html',{'todo':todo})

def edit(request,pk):
	todo=Todo.objects.get(pk=pk)
	if request.method=='POST':
		
			todo.number=request.POST['srnumber']
			todo.title=request.POST['title']
			todo.category=request.POST['category']
			todo.description=request.POST['description']
			
			todo.save()
			msg='update successfully.'
			return render(request,'edit.html',{'todo':todo,'msg':msg})
		
	return render (request,'edit.html',{'todo':todo})

def delete(request,pk):
	todo=Todo.objects.get(pk=pk)
	todo.delete()
	return redirect(read)		