from django.shortcuts import render
from django.http import HttpResponse
from Universities.models import University

# Create your views here.
def profile(request, universityid):
	university = University.objects.get(id=universityid)
	return render(request, 'Universities\\profile.html', {'university': university})
	
