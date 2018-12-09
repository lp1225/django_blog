from django.contrib import admin
from .models import Post, Category, Tag

# 注册admin后台模型


class PostAdmin(admin.ModelAdmin):
    """
    定制后台显示信息
    """
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

