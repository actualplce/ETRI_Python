from django.contrib import admin
from .models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')

#데코레이터 대신 admin.site.register(Bookmark,BookmarkAdmin)