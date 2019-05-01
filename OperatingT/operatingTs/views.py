from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import indexForm
from .forms import signinForm
from django.http import HttpResponse, JsonResponse
from .models import *

'''验证是否登录的装饰器'''
def check_user(func):
    def inner(*args, **kwargs):
        username = args[0].session.get("login_user", "")
        print(username)
        if username == "":
            args[0].session["path"] = args[0].path
            return  redirect('/')
        return func(*args, **kwargs)
    return inner

def signin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        schoolNo = request.POST.get('schoolNo')
        className = request.POST.get('className')
        telNo = request.POST.get('telNo')
        password = request.POST.get('password')
        #选择判断注册用户是否存在
        getschoolNO = User.objects.filter(user_id=str(schoolNo))
        if getschoolNO:
            print('已经注册过了,直接登陆')
            return JsonResponse({'code': "1"})
        else:
            createUser=User(
                user_name=str(name),
                user_id=str(schoolNo),
                user_class=str(className),
                user_phone=str(telNo),
                user_pwd=str(password),
                user_type='student',
                # property=''
                )
            createUser.save()
            return JsonResponse({'code': "0"})
    else:
        return render(request,'signin.html')

def login(request):
    # fuck!!!!不要动这行!!!!!
    if request.method == 'GET' and request.GET.get('csrfmiddlewaretoken'):
        return redirect('/')
    if request.method == 'POST':
        schoolNo = request.POST.get('schoolNo')
        password = request.POST.get('password')
        character = request.POST.get('character')
        #学号是否存在:
        if User.objects.filter(user_id=str(schoolNo)):
            if str(User.objects.get(user_id=str(schoolNo)).user_type) == str(character):
                if str(User.objects.get(user_id=str(schoolNo)).user_pwd) == str(password):
                    print('登陆成功')
                    # 先登录成功,再存cookie!!!!
                    request.session["login_user"] = "123"
                    return JsonResponse({'code': "0"})
                else:
                    print('密码错误')
                    return JsonResponse({'code': "1"})
            else:
                print('你不是'+str(character))
                JsonResponse({'code': "2"})
        else:
            print('没这个人')
            return JsonResponse({'code': "3"})
    else:
        return render(request, 'login.html')


'''论坛版块'''
#@check_user
def forum(request):
    print(request.body)
    question_list=Question.objects.all()
    ans={}
    for question in question_list:
        ans[question.question_id]=Ans.objects.filter(question_id=question.question_id)[0].content
    return render(request, 'forum.html',{
        'question_list':question_list,
        'ansDict':ans,
        'range':range(5)
    })

@check_user
def course(request):
    lessons = Lesson.objects.all()
    courses = list()
    result = dict()
    color_css = ['bk-clr-one', 'bk-clr-two', 'bk-clr-three', 'bk-clr-four']
    color_count = 0
    for lesson in lessons:
        one_course = {
            'name': lesson.name,
            'file': lesson.file,
            'color': color_css[color_count%4]
        }
        color_count += 1
        courses.append(one_course)
    result['courses'] = courses
    return render(request, 'courses.html', result)
