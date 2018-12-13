from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=70)
    body = models.TextField()  # 文章正文
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()  # 最后修改时间
    excerpt = models.CharField(max_length=200, blank=True)  # 允许为空
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)  # User是用户内置的

    views = models.PositiveIntegerField(default=0)  # 记录阅读量

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        自定义
        """
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views']) # 只更新这个字段

    class Meta:
        ordering = ['-created_time', 'title']

