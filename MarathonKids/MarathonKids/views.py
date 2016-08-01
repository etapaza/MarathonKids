from django.shortcuts import render
from django.http import HttpResponse
from Universities.models import University, Counter

# Create your views here.
def index(request):
	print("trying to render")
	
	universities = University.objects.extra(
		select={'points': 'kids_enrolled + money_raised + social_media'},
		order_by=['-points',],
	)
	counter = Counter();
	return render(request, 'MarathonKids\\index.html', {
		'universities': universities,
		'counter': counter,
		'user': request.user
	})
