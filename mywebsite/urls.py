"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django_web.views import index
from django_web import views
from django.conf.urls import include
#导入views.py文件中的index函数

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index), #在url中凡是以url开头的访问都使用index函数来处理该请求
    path('blog/', views.blog_index),
    url(r'^guestbook/', include('guestbook.urls', namespace='guestbook')), # 'guestbook.urls' --》app的名字
    # 表示在url地址中所有guestbook的都交给guestbook下面的url来处理，后面的逗号不要省略
]
