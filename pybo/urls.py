from django.urls import path
from . import views

app_name = 'pybo'  #네임스페이스(앱별칭)

urlpatterns = [
   path('',views.index, name='index'),
   path('<int:question_id>/',views.detail, name='detail'),  #질문번호링크
   path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),  #설문답변링크 
   
   
   
   ]
