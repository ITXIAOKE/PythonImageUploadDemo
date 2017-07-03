from django.db import models


# 图片的模型
class PicInfo(models.Model):
    # 上传图片记录
    pcontent = models.ImageField(upload_to='booktest/')
