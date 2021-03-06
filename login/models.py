from django.db import models

# Create your models here.

class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100, unique=True)
    sex = models.CharField(max_length=10, choices=gender, default="男")
    created_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        # 按创建时间反序排列,最近的优先显示
        ordering = ["-created_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=255)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:

        ordering = ["-created_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"