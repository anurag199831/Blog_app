from django.contrib import admin
from .models import Blog,Category,UserData

class BlogAdmin(admin.ModelAdmin):
    exclude = ('creation_date',)
    list_display = ('title', 'category', 'author', 'creation_date')
# Register your models here.

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(UserData)