# demo
first upload at 20170928_1712

## software version:
+ python 3.5.2
+ django 1.11.3
+ Markdown 2.6.9
+ Pygments 2.2.0

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