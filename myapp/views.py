from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from myapp import models

# Create your views here.

#basic return when URL:http://ipaddress:port/login
def login(request):
	return render(request, 'login.html')

# set var in html
def hello_add(request):
	context = {}
	context['hello'] = 'Hello World!'
	if request.method == "POST":
		#if request.POST.has_key('add'):
		if 'add' in request.POST:
			username = request.POST.get("username", None)
			password = request.POST.get("password", None)
			models.TestInfo.objects.get_or_create(user=username, pwd=password)
		#elif 'delete' in request.POST:
		#	deleteuser = request.POST.get("deleteuser", None)
		#	models.TestInfo.objects.filter(user=deleteuser).delete()
	#context["hellodata"] = models.TestInfo.objects.all()
	context["hellodata"] = models.TestInfo.objects.order_by("user")
	return render(request, 'hello.html', context)

def hello_delete(request, a=None, b=None):
	context2 = {}
	#if a not in context2:
	#	return HttpResponse("error!")
	models.TestInfo.objects.filter(user=a,pwd=b).delete()
	c = "id " + "\"" + str(a) + "\"" + " has been deleted"
	context2['item'] = c
	#return HttpResponse(str(c))
	return render(request, 'hello2.html', context2)
#################################name test#####################################
#def hello2(request):
#	return render(request, 'hello2.html')
#################################name testend#####################################

##############################add test#########################################
# url: http://10.181.3.91:8000/add/?a=4&b=5
def add(request):
 	a = request.GET.get('a', 0)
 	b = request.GET.get('b', 0)
 	c = int(a) + int(b)
 	return HttpResponse(str(c))

# url: http://10.181.3.91:8000/add/4/5/
def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
##############################add test end#########################################

#POST in the html
#set some data
#user_list = [
#	{"user": "hunter", "pwd": "abc"},
#	{"user": "jack", "pwd": "ABC"},
#]

def test(request):
	if request.method == "POST":
		#catch the var from the POST,if not,None
		username = request.POST.get("username", None)
		password = request.POST.get("password", None)
		#temp = {"user": username, "pwd": password}
		#user_list.append(temp)
		#create data in the database
		models.UserInfo.objects.create(user=username, pwd=password)
	# load data from the database
	user_list = models.UserInfo.objects.all()
	return render(request, 'login2.html', {"userdata": user_list})

def access_error(request):
	return HttpResponse("Page error!")

############################## myapp_blog ##############################
def mytest(request):
	context_mytest = {}
	context_mytest['welcome'] = '欢迎访问（修改字段）'
	context_mytest['article_list'] = models.Article_Blog.objects.all().order_by('-created_time')
	return render(request, 'blog/mytest.html', context_mytest)

def detail(request, pk):
	context_detail = {}
	# 其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
	context_detail['post'] = get_object_or_404(models.Article_Blog, pk=pk)
	return render(request, 'blog/detail.html', context_detail)


############################## myapp_blog end ##############################