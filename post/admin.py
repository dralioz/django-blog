from django.contrib import admin
from .models import Post 

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","publishing_date","slug"]
    list_display_links = ["publishing_date"]
    list_filter = ["publishing_date"]
    search_filter = ["title","content"]
    list_editable = ["title"]
    # prepopulated_fields = {'slug':('title',)}
    
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)