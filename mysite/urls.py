from django.contrib import admin
from django.urls import path, include
from .views import HomeView     #추가

# from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),       #추가(메인페이지)
    path('bookmark/', include('bookmark.urls')),  #추가됨, include가있어야 다른 app에 연결가능.
    path('blog/', include('blog.urls')),
    #class-based views
    # path('bookmark/', BookmarkLV.as_view(),name='index'),
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),

]
