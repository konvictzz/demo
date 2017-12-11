from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from services import models

# Create your views here.

def url(request):
	context_url = {}
	context_url['section'] = 'url' 
	# 因为 models 文件定义了 Meta ，所以无需指定 order_by
	#context_url["app_url"] = models.Server_URLs.objects.all().order_by('servertype')
	context_url["url_list"] = models.Server_URLs.objects.all()
	return render(request, 'services/url.html', context_url)

def environment_type(request, pk):
	context_environment = {}
	context_environment['section'] = 'url' 
	type = get_object_or_404(models.Server_Type, pk=pk)
	context_environment["url_list"] = models.Server_URLs.objects.filter(servertype=type)
	return render(request, 'services/url.html', context_environment)