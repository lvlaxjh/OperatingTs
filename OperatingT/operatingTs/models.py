from django.db import models

class User(models.Model):
    user_id = models.CharField("学号", primary_key = True)
    user_pwd = models.CharField("密码", max_length = 32, null = False)
    user_name = models.CharField("姓名", max_length = 32, null = False)
    user_class = models.CharField("班级", max_length = 32, null = False)
    user_phone = models.CharField("手机号", max_length = 32, null = False)
    user_type = models.CharField("类型", max_length = 32, null = False)
    properties = models.TextField("已下载课程", default = '[]')

    def __str__(self):
        return str(self.user_id)

class Lesson(models.Model):
    lesson_id = models.AutoField("课程唯一标识符", primary_key = True)
    name = models.CharField("课程名", max_length = 256, null = False, default = "Lesson")
    file = models.TextField("文件名", null = False)

    def __str__(self):
        return str(self.lesson_id)