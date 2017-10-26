from django import template
from .. import models

# 为了能够通过 {% get_recent_posts %} 的语法在模板中调用这个函数，必须按照 Django 的规定注册这个函数为模板标签
register = template.Library()

@register.simple_tag
def get_environment_type():
	return models.Server_Type.objects.all()