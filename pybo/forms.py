from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):  #모델폼
    class Meta:             #장고 모델폼은 Meta클래스 반드시!
        model = Question
        fields = ['subject', 'content']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control','rows':10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }    #한국말로 바꿔줌.

class AnswerForm(forms.ModelForm):    #답변등록 장고 폼
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }