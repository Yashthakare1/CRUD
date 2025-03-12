from django.shortcuts import render, redirect
from .models import Employees
# Create your views here.

def Index(request):
    emp=Employees.objects.all()

    context = {
        'emp':emp
    }
    return render(request,'index.html',context)


def Add(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        emp = Employees(
            name=name,email=email,phone=phone,address=address
        )
        emp.save()
        return redirect('home')
    return render(request,'index.html')

def Edit(request):
    emp = Employees.objects.all()

    context = {
        emp:'emp'
    }
    return render(request,'index.html',context)

def Update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        emp = Employees(
            id = id,name=name,email=email,address=address,phone=phone
        )
        emp.save()
        return redirect('home')

    return render(request,'index.html')

def Delete(request,id):
    emp = Employees.objects.filter(id = id)
    emp.delete()
    return redirect('home')
    context = {
        emp:'emp'
    }
    return render(request,'index.html',context)