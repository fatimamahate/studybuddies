from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'category', 'difficulty','post_created_on')
    search_fields = ['title', 'main_body']
    list_filter = ('status','category', 'post_created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('main_body',)

# Register your models here.
# admin.site.register(Post)
admin.site.register(Comment)



