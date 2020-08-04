from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from user.models import CustomUser


def question_read(request): #(최종인)
    questions = Question.objects.all() #question에 있는 객체들을 다 불러온다
    context = {'question' : questions } # ''안에있는건 내가 정의한거: question's' 인이유는 read에서 모든 게시물들을 보니깐 
    return render(request, 'question/read.html', context)

def question_read_one(request, pk): #(최종인)
    question = get_object_or_404(Question, pk = pk) 
    context = {'question' : question }  #question's'가 아닌이유는 read_one에서 개별 항목에 대한 것을 볼것이기 때문
    
    
    return render(request, 'question/read_one.html', context) 

    

def update(request):
    return render(request, 'question/update.html')


def question_create(request): #read를 구현시키기 위해 임의로 create 설정함/나중에 선주누나방식으로 채워짐. (최종인)
    if request.method == 'POST' or request.session.get('user', False): 
        title = request.POST['title']
        author = get_object_or_404(CustomUser, username = request.session['user'])
        content = request.POST['content']
        

        question = Question(
            author = author,
            title = title,
            content = content,
            

        )

        question.save()

        return redirect('question_read')
    else:
        return render(request, 'question/create.html')


     