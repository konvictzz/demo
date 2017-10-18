# -*- coding:UTF-8 -*-

from django import template
from .. import models

# 为了能够通过 {% get_recent_posts %} 的语法在模板中调用这个函数，必须按照 Django 的规定注册这个函数为模板标签
register = template.Library()

# 注册函数
@register.simple_tag
def get_recent_posts(num=5):
	# 从数据库根据 created_time 字段，倒叙返回 num 篇文章，默认为 5
	return models.Article_Blog.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
	# 精确到月份，降序排列
	return models.Article_Blog.objects.dates('created_time', 'month', order='DESC')
	#return models.Article_Blog.objects.dates('created_time', 'day', order='DESC')

@register.simple_tag
def get_categories():
	return models.Category.objects.all()

