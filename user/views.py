from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.decorators import login_required 
from .forms import MyUserForm

# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return redirect('todo')

@login_required
def profile(request):
    return render(request,'./user/profile.html')
    
    return render(request,'./user/profile.html')
def user_login(request):
    message,username='',''
    message = '登入'

    if request.method == 'POST':
        print('POST')
        if request.POST.get('login'):
            username = request.POST.get('username')
            password = request.POST.get('password')

            print(username, password)
            if username == '' or password == '':
                message = '帳號或密碼不的為空'
            else:
                user = authenticate(request,username=username,password=password)
                if user is None:
                    if User.objects.filter(username=username):
                        message='密碼有誤'
                    else:
                        
                        message='帳號有錯!!'
                else:
                    login(request,user)
                    message='登入中... ...'
                    return redirect('todo')
            # 1.檢查帳密是否正確
            # 2.是否有該使用者
            # 3.匹配密碼進行登入

            print('login')
        elif request.POST.get('register'):
            return redirect('register')

    return render(request, './user/login.html', {'message': message,'username':username})


def user_register(request):

    form = MyUserForm()
    message = ''

    if request.method == 'GET':
        print('GET')
    elif request.method == 'POST':
        print('POST')
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email=request.POST.get('email')

        if len(password1) < 8:
            message = '密碼少於8字元'
        elif password1 != password2:
            message = '兩次密碼不同'
        else:
            if User.objects.filter(username=username).exists():
                message = '帳號重複，請換其他帳號'
            else:
                user = User.objects.create_user(username=username, password=password1,email=email)
                user.save()
                message = '註冊成功'
                login(request,user)
                return redirect('todo')

        # 註冊功能
        # 兩次密碼是否相同
        # 密碼不可少於8個字元
        # 使用者名稱不能重複

    return render(request, './user/register.html', {'form': form, 'message': message})
