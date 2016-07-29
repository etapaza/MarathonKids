from django.shortcuts import render, redirect
from django.http import HttpResponse
from Universities.models import University
from django.contrib import auth
from datetime import datetime

# Create your views here.
def profile(request, universityid):
	university = University.objects.get(id=universityid)
	return render(request, 'Universities\\profile.html', {'university': university})

def create(request):
	University.objects.all().delete()
	University.objects.create_user(
		id=0,
		username='umich.edu',
		password='goblue',
		name='University of Michigan',
		points=75,
		kids_enrolled=0,
		miles_ran=0,
		date_joined=datetime.now(),
		email='',
		first_name='',
		last_name='',
		is_active=True,
		is_staff=False,
		is_superuser=False,
	)
	University.objects.create_user(
		id=1,
		username='msu.edu',
		password='spartyon',
		name='Michigan State University',
		points='50',
		kids_enrolled=0,
		miles_ran=0,
		date_joined=datetime.now(),
		email='',
		first_name='',
		last_name='',
		is_active=True,
		is_staff=False,
		is_superuser=False,
	)
	University.objects.create_user(
		id=2,
		username='osu.edu',
		password='buckeye',
		name='Ohio State University',
		points=60,
		kids_enrolled=0,
		miles_ran=0,
		date_joined=datetime.now(),
		email='',
		first_name='',
		last_name='',
		is_active=True,
		is_staff=False,
		is_superuser=False,
	)
	University.objects.create_user(
		id=3,
		username='duke.edu',
		password='bluedevil',
		name='Duke University',
		points=69,
		kids_enrolled=0,
		miles_ran=0,
		date_joined=datetime.now(),
		email='',
		first_name='',
		last_name='',
		is_active=True,
		is_staff=False,
		is_superuser=False,
	)
	University.objects.create_user(
		id=4,
		username='uoregon.edu',
		password='duck',
		name='University of Oregon',
		points=43,
		kids_enrolled=0,
		miles_ran=0,
		date_joined=datetime.now(),
		email='',
		first_name='',
		last_name='',
		is_active=True,
		is_staff=False,
		is_superuser=False,
	)
	return redirect('MarathonKids-home')

def login(request):
	print('Received', request)
	print('Received', request.POST)
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	auth.login(request, user)
	return redirect(request.META['HTTP_REFERER'])

def logout(request):
	auth.logout(request)
	return redirect(request.META['HTTP_REFERER'])

def update(request):
	print('Updating:', request.user)
	print(request.POST)
	to_update = University.objects.get(id=request.user.id)
	if request.POST.get('kids-value'):
		to_update.kids_enrolled += int(request.POST['kids-value'])
	else:
		to_update.miles_ran += int(request.POST['miles-value'])
	to_update.save()
	return profile(request, request.user.id)
