from django import forms
#forms.py现在貌似没什么用
#登录界面表单
class indexForm(forms.Form):
    # peopleID = forms.CharField()
    schoolNo = forms.Field()
    password = forms.Field()
    character = forms.Field()
    character = forms.Field()

#注册界面表单
class signinForm(forms.Form):
    name = forms.Field()
    schoolNo = forms.Field()
    className = forms.Field()
    telNo = forms.Field()
    password = forms.Field()

