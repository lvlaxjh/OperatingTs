from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import indexForm
from .forms import signinForm
from django.http import HttpResponse
from .models import *

'''验证是否登录的装饰器'''
def check_user(func):
    def inner(*args, **kwargs):
        username = args[0].session.get("login_user", "")
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
        return HttpResponse('123')
        #
        # if schoolNo and password:
        #     return HttpResponse('123')
    else:
        return render(request,'./signin/index.html')
# def spost(request):
#     form = signinForm(request.POST)
#     if form.is_valid():
#         return HttpResponse('123fuck')
#     else:
#         # print(form.errors.get_json_data())
#         # print(form.errors)
#         print('验证失败')
#         return HttpResponse('123123')
# class SigninView(View):
#     def get(self,request):
#         return render(request,'./signin/index.html')
def login(request):
    if request.method == 'POST':
        schoolNo = request.POST.get('schoolNo')
        password = request.POST.get('password')
        request.session["login_user"] = "123"
        if schoolNo and password:

            return redirect('/forum')
    else:
        return render(request, './login/index.html')
# class IndexView(View):
#     def get(self,request):
#         return render(request,'./login/index.html')
#         # return render(request, 'indextest.html')
#
#     def post(self,request):
#         form = indexForm(request.POST)
#         if form.is_valid():
#             return HttpResponse('fuck')示例
#         else:
#             #print(form.errors.get_json_data())
#             # print(form.errors)
#             print('验证失败')
#             return HttpResponse('123')

'''论坛版块'''
@check_user
def forum(request):
    print(request.body)
    question_list=Question.objects.all()
    ans={}
    for question in question_list:
        ans[question.question_id]=Ans.objects.filter(question_id=question.question_id)[0].content
    return render(request, './forun/index.html',{
        'question_list':question_list,
        'ansDict':ans,
        'range':range(10)
    })
