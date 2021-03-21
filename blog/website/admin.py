from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title','categories','approved']
    search_fields = list_display

    #def get_queryset(self, request):
        #return Post.objects.filter(approved=True)
    
admin.site.register(Post, PostAdmin)

