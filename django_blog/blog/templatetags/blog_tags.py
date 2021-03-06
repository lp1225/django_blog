from ..models import Post, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    """
    最新文章
    """
    # 必须规定为django的模板文件
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    """
    归档模板
    """
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    """
    分类
    """
    return Category.objects.all()
