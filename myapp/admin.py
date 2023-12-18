from django.contrib import admin
from .models import Blogs


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    class Meta:
        model = Blogs
        list_display = ['tittle', 'reference']


admin.site.register(Blogs, BlogAdmin)
