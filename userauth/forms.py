# -*- coding:UTF-8 -*-

from django import forms

# 使用 PasswordInput 控件来渲染 HTMLinput 元素，包含 type="password" 属性
# django 规定，必须继承自 forms.Form 类或者 forms.ModelForm 类
class  LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)