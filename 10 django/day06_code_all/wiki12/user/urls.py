from django.conf.urls import url
from . import views

urlpatterns=[
    #http://127.0.0.1:8000/user/reg
    url(r'^reg$', views.reg_view)

]
