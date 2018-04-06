
from django.conf.urls import url
from . import views
app_name = 'guestbook'
urlpatterns = [
    url(r'^index/', views.index, name='index'),   #不要忘了逗号
    url(r'^create/$', views.create, name='create'),
    url(r'^save/$', views.save, name='save'),
]