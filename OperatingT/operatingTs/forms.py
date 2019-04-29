from django import forms

#登录界面表单
class indexForm(forms.Form):
    # peopleID = forms.CharField()
    schoolNo = forms.Field()
    password = forms.Field()
    character = forms.Field()
    character = forms.Field()

#注册界面表单
class signinForm(forms.Form):
    pass