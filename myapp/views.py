import markdown
import logging
from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from myapp import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils import timezone

# login required
# If the user isn’t logged in, redirect to 'settings.LOGIN_URL'

# logging
logger = logging.getLogger(__name__)

# Create your views here.

# basic return when URL:http://ipaddress:port/login
def login(request):
	return render(request, 'login.html')

@login_required
def demo(request):
	context_demo = {}
	context_demo['section'] = 'infopage'
	return render(request, 'infopage.html', context_demo)

#def demoshow(request):
#	logger.info("custom logging")
#	logger.info("temppage successfully")
#	return render(request, 'temp.html', {'section': 'temp'})

class DemoShowView(LoginRequiredMixin, TemplateView):
	template_name = "temp.html"

	def get_context_data(self, **kwargs):
		context_demoshow = super(DemoShowView, self).get_context_data(**kwargs)
		logger.info("custom logging")
		context_demoshow['title'] = 'Demo Page'
		context_demoshow['section'] = 'demoshow'
		context_demoshow['now'] = timezone.now()
		context_demoshow['viewname'] = __name__
		logger.info("load context successfully")
		return context_demoshow

# set var in html
def hello_add(request):
	context = {}
	context['hello'] = 'Hello World!'
	context['section'] = 'home'
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
	context2['section'] = 'home'
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
def add2(request, a=0, b=0):
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

def homepage(request):
	context_homepage = {}
	context_homepage['welcome'] = "welcome"
	return render(request, 'homepage.html', context_homepage)

def access_error(request):
	return HttpResponse("Page error!")

############################## myapp_blog ##############################
def blogindex(request):
	context_mytest = {}
	context_mytest['welcome'] = '欢迎访问（修改字段）'
	# 加入 section 做 nav 判断
	context_mytest['section'] = 'blog'
	context_mytest['article_list'] = models.Article_Blog.objects.all().order_by('-created_time')
	return render(request, 'blog/mytest.html', context_mytest)

def detail(request, pk):
	context_detail = {}
	context_detail['section'] = 'blog'
	# 其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
	context_detail['post'] = get_object_or_404(models.Article_Blog, pk=pk)
	# 增加markdown语法，这里使用了三个拓展，分别是 extra、codehilite、toc
	# extra 本身包含很多拓展，而 codehilite 是语法高亮拓展，这为后面的实现代码高亮功能提供基础
	# 而 toc 则允许我们自动生成目录
	# 需要将html中的 {{ post.content }} 改成 {{ post.content|safe }}，告诉 django 这段文本使安全的
	# 需要安装 Pygments 才能做到插入的代码高亮，安装方法： pip install Pygments
	context_detail['post'].content =  markdown.markdown(context_detail['post'].content,
														extensions = [
															'markdown.extensions.extra',
															'markdown.extensions.codehilite',
															'markdown.extensions.toc',
															]
														)
	return render(request, 'blog/detail.html', context_detail)

# 操作页面侧边栏的 时间归档
def archives(request,year,month):
	context_archives = {}
	context_archives['section'] = 'blog'
	# Python 中类实例调用属性的方法通常是 created_time.year
	# 由于这里作为函数的参数列表，所以 Django 要求我们把点替换成了两个下划线
	# 经过测试，字段支持 year / month / hour / minute
	context_archives['article_list'] = models.Article_Blog.objects.filter(created_time__year = year,
																	   created_time__month = month
																	   ).order_by('-created_time')
	return render(request, 'blog/mytest.html', context_archives)

# 操作页面侧边栏的 文章分类
def category(request, pk):
	context_category = {}
	context_category['section'] = 'blog'
	# 获取 category， 传入对应的pk值，如存在则返回，不存在返回 404
	cate = get_object_or_404(models.Category, pk=pk)
	context_category['article_list'] = models.Article_Blog.objects.filter(category=cate).order_by('-created_time')
	return render(request, 'blog/mytest.html', context_category)


############################## myapp_blog end ##############################