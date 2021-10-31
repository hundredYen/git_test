from django.contrib import admin
from .models import Book
# Register your models here.


class BookManager(admin.ModelAdmin):
    #列名
    list_display = ['id', 'title', 'pub', 'price', 'market_price', 'is_activate']
    #链接到修改页面的字段
    list_display_links = ['id', 'title']
    #右边栏过滤器
    list_filter = ['pub', 'title', 'is_activate']
    #搜索框
    search_fields = ['title', 'pub']
    #可编辑列表 和超链接字段冲突
    list_editable = ['price', 'market_price']

admin.site.register(Book, BookManager)