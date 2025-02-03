from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from wiki.models import Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('conteudo_post',)
    

# Register your models here.
admin.site.register(Post, PostAdmin)
