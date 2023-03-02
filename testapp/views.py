from django.shortcuts import render, HttpResponseRedirect
from.forms import EmployeeRegistration
from .models import User
# This is for add and show all data
def add_show(request):
    if request.method == 'POST':
        fm=EmployeeRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm, email=em,password=pw)
            fm.save()
            fm=EmployeeRegistration() 
    else:
        fm=EmployeeRegistration()  
    stud= User.objects.all()
    return render (request, 'addandshow.html',{'form':fm,'stu':stud, })



#this will update and Edit 

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm =EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save() 
    else:
        pi = User.objects.get(pk=id)
        fm =EmployeeRegistration(instance=pi)                 
    return render(request, 'update.html',{'form':fm})



# This fun will delete the data 

def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
       