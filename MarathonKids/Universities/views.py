from django.shortcuts import render, redirect
from django.http import HttpResponse
from Universities.models import University
from django.contrib import auth

# Create your views here.
def profile(request, universityid):
	university = University.objects.get(id=universityid)
	return render(request, 'Universities\\profile.html', {'university': university})

def login(request):
	print('Received', request)
	print('Received', request.POST)
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	auth.login(request, user)
	return redirect('MarathonKids-home')

def logout(request):
	auth.logout(request)
	return redirect('MarathonKids-home')

def edit(request):
	return HttpResponse('Edit page')
