from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from userauth.forms import LoginForm

# Create your views here.
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