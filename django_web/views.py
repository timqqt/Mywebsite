from django.shortcuts import render
from django.shortcuts import render
from django_web.models import BlogsPost


def index(request):
    return render(request, 'index.html')
# Create your views here.


# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request, 'index_blog.html', {'blog_list': blog_list})   # 返回index.html