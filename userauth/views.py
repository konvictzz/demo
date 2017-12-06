from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from userauth.forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
	context_user_login = {}
	if request.method == "POST":
		form = LoginForm(request.POST)
		# 判断是否无效
		# 执行校验器，检查 form 中的数据是否符合定义规则
		if form.is_valid():
			# 如果 form.is_valid() 为True
			# 通过 form.cleaned_data 这个dict来获取数据自动转型
			cd = form.cleaned_data
			# authenticate() 检查用户认证信息，如果用户是正确的则返回一个用户对象
			user = authenticate(username = cd['username'],
								password = cd['password'])
			if user is not None:
				# 使用 is_active 属性来检查用户是否可用
				if user.is_active:
					# login() 将用户设置到当前的会话（session）中
					# 调用login()方法集合用户到会话（session）中然后返回一条成功消息
					login(request, user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	context_user_login['form'] = form
	return render(request, 'userauth/login.html',context_user_login)

# login_required 装饰器（decorator）会检查当前用户是否通过认证
# 如果用户通过认证，它会执行装饰的视图（view）
# 如果用户没有通过认证，它会把用户重定向到带有一个名为 next 的 GET 参数的登录 URL，该 GET 参数保存的变量为用户当前尝试访问的页面URL
# 通过这些动作，登录视图（view）会将登录成功的用户重定向到用户登录之前尝试访问过的URL
# 请记住我们在登录模板（template）中的登录表单（form）中添加的隐藏<input>就是为了这个目的。

# 定义了一个section变量。我们会使用该变量来跟踪用户在站点中正在查看的页面
# 多个视图（views）可能会对应相同的section。这是一个简单的方法用来定义每个视图（view）对应的section
@login_required
def dashboard(request):
	return render(request, 'userauth/dashboard.html', {'section': 'dashboard'})