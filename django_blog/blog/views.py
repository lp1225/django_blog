from django.shortcuts import render, get_object_or_404
import markdown

from . models import Post, Category
from .. comments.forms import CommentForm


def index(request):
    """
    首页
    """
    # post_list = Post.objects.all().order_by('-created_time')  # 减法代表逆序
    post_list = Post.objects.all()
    return render(request, 'index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    # 转化为markdown语法
    post.body = markdown.markdown(post.body, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    # 获得post下的全部评论
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'detail.html', context=context)


def archives(request, year, month):
    """
    归档
    """
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})


def category(request, pk):
    """
    分类
    """
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})
