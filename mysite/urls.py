from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #추가
from django.conf import settings #추가 #static(settings~부분활성화.
from .views import HomeView     #추가
from mysite.views import UserCreateView, UserCreateDoneTV   #추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/',UserCreateView.as_view(),name='register'),
    path('accounts/register/done/',UserCreateDoneTV.as_view(),name='register_done'),
    path('', HomeView.as_view(), name='home'),       #추가(메인페이지)
    path('bookmark/', include('bookmark.urls')),  #추가됨, include가있어야 다른 app에 연결가능.
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')), #추가



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  #추가, 포토앱.
