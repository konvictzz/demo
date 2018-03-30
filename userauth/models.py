from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

# 这个方法需要删除数据库重新makemigrations
#class CustomUser(AbstractUser):
#	telephone_number = models.CharField(max_length=20, blank=True, verbose_name='手机号码')
	#def __str__(self):
	#	return self.telephone_number

#	class Meta(AbstractUser.Meta):
#			pass

# 扩展现有User模型
class CustomUser(models.Model):
	user = models.OneToOneField(User,
								on_delete=models.CASCADE,
								related_name='customuser')
	telephone_number = models.CharField(max_length=20, blank=True, verbose_name='手机号码')

	class Meta:
		verbose_name = '其他信息'