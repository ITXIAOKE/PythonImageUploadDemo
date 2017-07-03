import time
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

# 显示上传图片视图函数
from booktest.models import PicInfo


def upload_img(request):
    return render(request, 'booktest/upload_img.html')


# 接受图片并将图片保存在mysql数据库中
def rec_img(request):
    pic = request.FILES.get('img')

    print("图片名字：%s" % pic.name)

    # 拼接出保存上传图片的路径
    path = '%s/booktest/%s' % (settings.MEDIA_ROOT, pic.name)

    # 创建文件
    with open(path, 'wb') as f:
        for c in pic.chunks():
            f.write(c)

    # 将上传图片的路径保存到mysql数据库中
    p = PicInfo()
    p.pcontent = 'booktest/%s' % pic.name
    p.save()

    return render(request, 'booktest/show_button.html')


def show_img(request):
    pic_show = PicInfo.objects.get(id=14)
    return render(request, 'booktest/show_img.html', {'pic_show': pic_show})
