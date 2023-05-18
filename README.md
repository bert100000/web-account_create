# TODOLIST APP

>2023/4/7
### 使用開發工具
- vscode 1.77.1
- python 3.8.16
- django 4.1.7

### 指令
- django-admin startproject todolist
- python manage.py runserver

### 新增app
- python manage.py startapp user
- settings.py [INSTALLED_APPS]
  - "user.apps.UserConfig"

### 進行資料庫同步
- python manage.py migrate

### 後台新增超級管理者
 - python manage.py createsuperuser

### 語系、時區變更(setting.py)
 - LANGUAGE_CODE = 'zh-Hant'
 - TIME_ZONE = 'Asia/Taipei'

 ### python manage.py shell 
 - from django.contrib.auth.models import User 
 - User.objects.all()
 - User.objects.get(id=1)
 - User.objects.filter(username='bert')


