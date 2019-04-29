from django.shortcuts import render
from django.views.generic import View
from .forms import indexForm
from django.http import HttpResponse

def signin(request):
    return render(request,'./signin/index.html')

class IndexView(View):
    def get(self,request):
        return render(request,'./login/index.html')
        # return render(request, 'indextest.html')

    def post(self,request):
        form = indexForm(request.POST)
        if form.is_valid():
            return HttpResponse('fuck')
        # else:
        #     #print(form.errors.get_json_data())
        #     # print(form.errors)
        #     print('验证失败')
        #     return HttpResponse('123')