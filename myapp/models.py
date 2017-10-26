# -*- coding:UTF-8 -*-

# 因为注释含有中文，所以需要编码声明coding:UTF-8
# 所有中文段落，符号也均为中文样式。反之，英文段落，符号为英文样式。
# 修改完需要通过命令创建数据库的表，如下：
# python manage.py makemigrations
# python manage.py migrate

# django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.

# 兼容python2，使python2.x 也像 python3 那个处理 unicode 字符，以便有更好地兼容性。
@python_2_unicode_compatible
# models.Model为固定写法，用法具体需要参考github上django的源码
class UserInfo(models.Model):
	#创建两个字段，最大长度32，类型是char
	user = models.CharField(max_length=32)
	pwd = models.CharField(max_length=32)
	def __str__(self):
		return self.user

@python_2_unicode_compatible
class TestInfo(models.Model):
	user = models.CharField(max_length=32)
	pwd = models.CharField(max_length=32)

@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(u'标题', max_length=256)
	# 允许为空
	content = models.TextField(u'内容', null=True, blank=True)
	pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
	def __str__(self):
		return self.title
		

########################### Blog Part ###########################
# 定义模型，我们这里需要 3个表格：文章（Article_Blog）、分类（Category）以及标签（tag）
@python_2_unicode_compatible
class Category(models.Model):
	# Django 要求模型必须继承 models.Model 类。
	# Category 只需要一个简单的分类名 name 就可以了。
	# CharField 指定了分类名 name 的市局类型为字符型，其余类型需要参考源码或官方文档。
	# max_length 指定字段最大长度，超过这个长度的分类名就不能被存入数据库。
	# 当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
	# Django 内置的全部类型可查看文档：
	# https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Tag(models.Model):
	# 标签 Tag 也需要一个 name
	# 在这里把长度设置为 100
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Article_Blog(models.Model):
	# 文章标题, 这里给到的长度 max_length 为 256
	title = models.CharField(max_length=256)

	# 文章正文，定义字段为TextField
	# 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是大段文本，因此使用 TextField 来存储大段文本。
	content = models.TextField()

	# 定义创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()

	# 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则报错
	# 指定 blank=True 参数值后可以允许为空
	excerpt = models.CharField(max_length=256, blank=True)
	
	# 关联分类和标签，之前已经完成定义。在这里，我们需要将文章对应的数据库表和分类、标签对应的数据库表关联起来。
	# 逻辑：
	# 规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以使用 ForeignKey，文章和分类的关系为一对多的关联关系。
	# 对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以使用 ManyToManyField，表明两者是多对多的关联关系。
	# 同时规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
	# 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
	# https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)

	# 文章作者，这里 User 是从 jango.contrib.auth.models 导入的。
	# django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
	# 这里我们通过 ForeignKey 把文章和 User 关联了起来。
	# 逻辑：规定一篇文章只能有一个作者，而一个作者可以有多篇文章，所以为一对多的关联关系
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title

	# 自定义 get_absolute_url 方法
	# 记得从 django.urls 中导入 reverse 函数
	def get_absolute_url(self):
		return reverse('myapp:detail', kwargs={'pk': self.pk})

########################### Blog Part end ###########################

########################### Blog comments ###########################



######################## Blog comments end ##########################