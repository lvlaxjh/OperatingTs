from django.shortcuts import render
from django.views.generic import View
from .forms import indexForm
from .forms import signinForm
from django.http import HttpResponse

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

        if schoolNo and password:

            return HttpResponse('123')
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
#             return HttpResponse('fuck')
#         else:
#             #print(form.errors.get_json_data())
#             # print(form.errors)
#             print('验证失败')
#             return HttpResponse('123')