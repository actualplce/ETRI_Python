from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Question
from django.utils import timezone  #시간

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html',context) 
    
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question_id)
# def answer_create(request,question_id):
#     """
#     pybo답변등록
#     """
#     question = get_object_or_404(Question, pk=question_id)   <-오타가 무엇이었을까..
#     question.answer_set.create(content=request.POST.get('content', create_date=timezone.now())   <-요기 'content') 틀렸다.
#     return redirect('pybo:detail',question_id=question.id) 