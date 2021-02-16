from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Question
from django.utils import timezone  #시간
from .forms import QuestionForm, AnswerForm    #질문,답 등록
from django.core.paginator import Paginator   #패이징기능

def index(request):
    """
    pybo 목록출력
    """
    # ---------------------------------- [edit] ---------------------------------- #
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # ---------------------------------------------------------------------------- #

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # ---------------------------------- [edit] ---------------------------------- #
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    # ---------------------------------------------------------------------------- #

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
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request,'pybo/question_detail.html',context)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail', question_id=question_id)

def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else :
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)