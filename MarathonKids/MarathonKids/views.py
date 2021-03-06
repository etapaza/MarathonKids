from django.shortcuts import render
from django.http import HttpResponse
from Universities.models import University, Counter

# Create your views here.
def index(request):
	print("trying to render")
	
	universities = University.order_by_points()
	counter = Counter();
	return render(request, 'MarathonKids\\index.html', {
		'universities': universities,
		'counter': counter,
		'user': request.user
	})
