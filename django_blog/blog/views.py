from django.shortcuts import render, get_object_or_404
import markdown
from django.http import HttpResponse

from . models import Post


def index(request):
    """
    首页
    """
    post_list = Post.objects.all().order_by('-created_time')  # 减法代表逆序
    return render(request, 'index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 转化为markdown语法
    post.body = markdown.markdown(post.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'post': post})
