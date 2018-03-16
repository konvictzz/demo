"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
#from django.contrib import admin
from . import views
#from django.contrib.auth.views import login, logout, password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

app_name = 'userauth'
urlpatterns = [
    #url(r'^login/$',views.user_login, name='login'),
    #url(r'',include('django.contrib.auth.urls')),
    
    # Django 1.11.0
    # login & logout
    #url(r'^login/$',login, name='login'),
    #url(r'^logout/$',logout, name='logout'),
    url('^login/$',auth_views.LoginView.as_view(template_name='userauth/login.html'), name='login'),
    url('^logout/$',auth_views.LogoutView.as_view(template_name='userauth/logged_out.html'), name='logout'),
    # dashboard
    url('^$',views.dashboard, name='dashboard'),
    # change password
    url('^password-change/$',auth_views.PasswordChangeView.as_view(template_name='userauth/password_change_form.html',
    															   success_url=reverse_lazy('userauth:password_change_done')), name='password_change'),
    url('^password-change/done/$',auth_views.PasswordChangeDoneView.as_view(template_name='userauth/password_change_done.html'),name='password_change_done'),
    # reset password & restore password urls
    # email address needs to match the user info
    url('^password-reset/$',auth_views.PasswordResetView.as_view(template_name='userauth/password_reset.html',
    															 email_template_name='userauth/password_reset_email.html', 
    															 subject_template_name='userauth/password_reset_subject.txt',
    															 success_url=reverse_lazy('userauth:password_reset_done')), name='password_reset'),
    url('^password-reset/done/$',auth_views.PasswordResetDoneView.as_view(template_name='userauth/password_reset_done.html'), name='password_reset_done'),
    url('^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.PasswordResetConfirmView.as_view(template_name='userauth/password_reset_confirm.html',
    																												 success_url=reverse_lazy('userauth:password_reset_complete')), name='password_reset_confirm'),
    url('^password-reset/complete/$',auth_views.PasswordResetCompleteView.as_view(template_name='userauth/password_reset_complete.html'), name='password_reset_complete'),
]
