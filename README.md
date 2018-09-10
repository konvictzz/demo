# demo
first upload at 20170928_1712

## software version:
+ python 3.5.2
+ django 1.11.3
+ Markdown 2.6.9
+ Pygments 2.2.0
+ elasticsearch 5.3.0
+ celery 4.2.1
+ eventlet 0.24.1

## settings
> path: `./demo/settings.py`  
> config field: `DATABASES`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': os.path.join("D:\\DBdata", 'demo.sqlite3'),
    }
}
```

## sync db
> cd path  
> python manage.py makemigrations  
> python manage.py migrate  

## startup
+ windows  
	> click the `startup.bat`
+ linux(centos7)  
	> no shell script(will be created later)  
	> please use `manage.py` to startup  
	> bash: cd path;python manage.py runserver 0.0.0.0:8000

## version
+ 1.3.11  
新增elasticsearch相关信息记录
+ 1.3.10  
新增URL和相关信息记录
+ 1.3.9  
增加用户字段
+ 1.3.8  
完善`日志记录`部分
+ 1.3.7  
增加`密码重置`功能  
需要和用户信息的邮箱地址匹配  
修改新增部分settings字段，邮件功能默认在控制台输出
+ 1.3.6  
增加`demo`页来记录一些`request`变量
+ 1.3.5  
增加`修改密码`功能
+ 1.3.4  
增加`login`和`logout`功能  
部分功能需要登录才能使用  
加入`blog`功能