from django.shortcuts import render,redirect
from blood_bank_management_system_app.models import blood
from django.contrib import messages




def bloods(request):
	if request.method=="POST":
		N=request.POST['FName']
		L=request.POST['LName']
		A=request.POST['age']
		S=request.POST['gender']
		M=request.POST['Mobile']
		E=request.POST['Email']
		G=request.POST['group']
		blood.objects.create(Fname=N,Lname=L,age=A,Gender=S,Mobile=M,email=E,group=G)
		messages.success(request,"You have Donated Successfully...")
		return redirect('blood')
	details=blood.objects.all()
	return render(request, 'blood.html',{'Details':details}) 

# def display(request):
# 	details=blood.objects.all()
# 	return redirect('blood')
