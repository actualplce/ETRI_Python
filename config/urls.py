from django.contrib import admin
from django.urls import path, include
from pybo import views   #추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),   #각 기능별 폴더에서 해당링크를 만들어관리하겠다.
]
