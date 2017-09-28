#from django.http import HttpResponse
from django.shortcuts import render

#basic return when URL:http://ipaddress:port/login
def login(request):
	return render(request, 'login.html')

#set var in html
def hello(request):
	context = {}
	context['hello'] = 'Hello World!'
	return render(request, 'hello.html', context)

#POST in the html
#set some data
user_list = [
	{"user": "hunter", "pwd": "abc"},
	{"user": "jack", "pwd": "ABC"},
]

def test(request):
	if request.method == "POST":
		username = request.POST.get("username", None)
		password = request.POST.get("password", None)
		temp = {"user": username, "pwd": password}
		user_list.append(temp)
	return render(request, 'login2.html', {"data": user_list})