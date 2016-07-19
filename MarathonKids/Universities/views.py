from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Universities.models import University
from django.contrib.auth import views as auth_views

# Create your views here.
def profile(request, universityid):
	university = University.objects.get(id=universityid)
	return render(request, 'Universities\\profile.html', {'university': university})

def login(request):
	if request.user.is_authenticated():
		return redirect('edit')
	else:
		return auth_views.login(request)

def edit(request):
	return HttpResponse('Edit page')
