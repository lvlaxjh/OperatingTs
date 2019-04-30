# Generated by Django 2.1.7 on 2019-04-30 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ans',
            fields=[
                ('ans_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ans_id')),
                ('content', models.TextField(verbose_name='content')),
                ('question_id', models.IntegerField(verbose_name='question_id')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_id', models.AutoField(primary_key=True, serialize=False, verbose_name='课程唯一标识符')),
                ('name', models.CharField(default='Lesson', max_length=255, verbose_name='课程名')),
                ('file', models.TextField(verbose_name='文件名')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False, verbose_name='question_id')),
                ('content', models.TextField(verbose_name='content')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='学号')),
                ('user_pwd', models.CharField(max_length=32, verbose_name='密码')),
                ('user_name', models.CharField(max_length=32, verbose_name='姓名')),
                ('user_class', models.CharField(max_length=32, verbose_name='班级')),
                ('user_phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('user_type', models.CharField(max_length=32, verbose_name='类型')),
                ('properties', models.TextField(default='[]', verbose_name='已下载课程')),
            ],
        ),
    ]
