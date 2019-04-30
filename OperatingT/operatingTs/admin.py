from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_type')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_id', 'name', 'file')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'content')

class AnsAdmin(admin.ModelAdmin):
    list_display = ('ans_id', 'content', 'question_id')

admin.site.register(User, UserAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Ans, AnsAdmin)
