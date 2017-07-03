from  django.conf.urls import url
from booktest import views

urlpatterns=[
    url(r'^upload_img/$',views.upload_img),
    url(r'^rec_img/$',views.rec_img),
    url(r'^show_img/$',views.show_img),
]