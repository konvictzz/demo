from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from services import models

# Create your views here.

def url(request):
	context_url = {}
	context_url["app_url"] = models.Server_URLs.objects.all().order_by('servertype')
	return render(request, 'services/url.html', context_url)