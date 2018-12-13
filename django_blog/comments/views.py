from django.shortcuts import render, get_object_or_404, redirect
from django_blog.blog.models import Post
from .models import Comment
from . forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)  # 用户提交的数据保存在request.POST中
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # 关联文章表
            comment.save()

            return redirect(post)
        else:
            # 数据不合法，重新渲染前端，提示错误信息
            comment_list = post.comment_set.all()  # 反向查询
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'detail.html', context=context)
    return redirect(post)
