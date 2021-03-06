from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import indexForm
from .forms import signinForm
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import *

Get_UserId = ''


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

#注册界面
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

#登录界面
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
                    Get_UserId = schoolNo
                    # 先登录成功,再存cookie!!!!
                    # 调试时可以先注释掉
                    request.session["login_user"] = schoolNo
                    return JsonResponse({'code': "0"})
                else:
                    print('密码错误')
                    return JsonResponse({'code': "1"})
            else:
                print('你不是'+str(character))
                return JsonResponse({'code': "2"})
        else:
            print('没这个人')
            return JsonResponse({'code': "3"})
    else:
        return render(request, 'login.html')

'''学习中心'''
def learningcenter(request):
    #检测该用户是否下载过课程:
    if User.objects.get(user_id=str(Get_UserId)).properties:
        print('没下载过课程')
    else:
        #查询用户所有下载过的课程
        for getOnelessonId in User_and_Lesson.objects.get(user_id=int(Get_UserId)).lesson_id:
            if Lesson.objects.get(lesson_id=getOnelessonId):
                lessonName = Lesson.objects.get(lesson_id=getOnelessonId).name
                lessonFile = Lesson.objects.get(lesson_id=getOnelessonId).file
    return render(request,'learningcenter.html')


'''论坛版块'''
@check_user
def forum(request):
    print(request.body)
    question_list=Question.objects.all()
    ans={}
    count = 0
    for question in question_list:
        ans[question.question_id]=Ans.objects.filter(question_id=count%2+1)[0].content
        count += 1
    return render(request, 'forum.html',{
        'question_list':question_list,
        'ansDict':ans,
        'range':range(5)
    })

'''调试时注释掉cookie检查'''
'''首页'''
@check_user
def course(request):
    lessons = Lesson.objects.all()
    courses = list()
    result = dict()
    user_id = request.session.get("login_user", "")
    color_css = ['bk-clr-one', 'bk-clr-two', 'bk-clr-three', 'bk-clr-four']
    color_count = 0
    for lesson in lessons:
        one_course = {
            'name': lesson.name,
            'lesson_id': lesson.lesson_id,
            'user_id': user_id,
            'color': color_css[color_count%4]
        }
        color_count += 1
        courses.append(one_course)
    result['courses'] = courses
    return render(request, 'courses.html', result)

def download(request):
    lesson_id = request.GET.get('lesson_id')
    user_id = request.GET.get('user_id')
    if len(lesson_id) > 0:
        lesson = Lesson.objects.filter(lesson_id = lesson_id)
        file = lesson[0].file
        if len(user_id) > 0:
            UAL = User_and_Lesson.objects.filter(lesson_id = lesson_id, user_id = user_id)
            if len(UAL) == 0:
                UAL = User_and_Lesson.objects.create(lesson_id = lesson_id, user_id = user_id)

        response = FileResponse(open('file/' + file, 'rb'))
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename="' + file + '"'  
        return response

#已下载课程
@check_user
def loadedcourse(request):
    course_ids=User_and_Lesson.objects.filter(user_id=request.session.get("login_user", ""))
    courses=[]
    result=[]
    color_css = ['bk-clr-one', 'bk-clr-two', 'bk-clr-three', 'bk-clr-four']
    color_count = 0
    for course_id in course_ids:
        courses.append(Lesson.objects.get(lesson_id=int(course_id.lesson_id)))
    for course in courses:
        one_course = {
            'name': course.name,
            'file': course.file,
            'color': color_css[color_count % 4]
        }
        color_count += 1
        result.append(one_course)
    return render(request, 'loadedcourse.html', {'courses':result})

def initial(request):
    users = [
        {
            'user_id': '2019001',
            'user_pwd': '2019001',
            'user_name': '张三',
            'user_class': '911',
            'user_phone': '133333',
            'user_type': 'student',
            'properties': '[]'
        },
        {
            'user_id': '2019002',
            'user_pwd': '2019002',
            'user_name': '李四',
            'user_class': '911',
            'user_phone': '133334',
            'user_type': 'student',
            'properties': '[]'
        },        
        {
            'user_id': '2019003',
            'user_pwd': '2019003',
            'user_name': '王五',
            'user_class': '911',
            'user_phone': '133335',
            'user_type': 'student',
            'properties': '[]'
        }
    ]
    lessons = [
        {
            'name': '离散数学',
            'file': '离散数学.pdf'
        },
        {
            'name': '中国近代史',
            'file': '中国近代史.pdf'
        },
        {
            'name': '计算机组成与结构',
            'file': '计算机组成与结构.pdf'
        },
        {
            'name': 'TensorFlow',
            'file': 'TensorFlow.pdf'
        },
    ]
    questions = [
        {
            'content': '天王盖地虎'
        },
        {
            'content': '猪鼻子插葱'
        }
    ]
    answers = [
        {
            'content': '宝塔镇河妖',
            'question_id': 1
        },
        {
            'content': '装象',
            'question_id': 2
        }
    ]

    for user in users:
        if len(User.objects.filter(user_id = user['user_id'])) == 0:
            User.objects.create(
                user_id = user['user_id'], 
                user_pwd = user['user_pwd'], 
                user_name = user['user_name'],
                user_class = user['user_class'],
                user_phone = user['user_phone'],
                user_type = user['user_type'],
                properties = user['properties']
                )

    for lesson in lessons:
        Lesson.objects.create(
            name = lesson['name'],
            file = lesson['file']
        )

    for question in questions:
        Question.objects.create(
            content = question['content']
        )

    for answer in answers:
        Ans.objects.create(
            content = answer['content'],
            question_id = answer['question_id']
        )

    return HttpResponse('Successful!!')