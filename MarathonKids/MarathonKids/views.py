from django.shortcuts import render
from django.http import HttpResponse
from Universities.models import University

# Create your views here.
def index(request):
	print("trying to render")
	universities = University.objects.all()
	return render(request, 'MarathonKids\\index.html', {"universities":universities})
	