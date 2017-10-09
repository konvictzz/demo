@echo off

:: Enter current path
cd /d %cd%
echo startup...
python manage.py runserver 0.0.0.0:8000