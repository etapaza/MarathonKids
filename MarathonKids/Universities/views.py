from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from Universities.models import University

# Create your views here.
def profile(request, universityid):
	university = University.objects.get(id=universityid)
	return render(request, 'Universities\\profile.html', {'university': university})

def login(request):
	if request.user.is_authenticated():
		return redirect('edit')
	else:
		pass
@login_required
def edit(request):
	return HttpResponse('Edit page')
