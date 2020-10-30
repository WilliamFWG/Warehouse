from django.shortcuts import render,redirect
from polls.models import Question,Choice

# Create your views here.

def index(request):
    #get the questions from models and order by 'pub_date' decending order
    questions = Question.objects.order_by('-pub_date')
    return render(request,'index.html',{'questions': questions})

def details(request,question_id):
    questions = Question.objects.get(id= question_id)
    return render(request,'details.html',{'questions':questions})

def votes(request,question_id):
    questions = Question.objects.get(id= question_id)
    choice_id = request.POST.get('choice_id')
    choice = questions.choice_set.get(id=choice_id)
    choice.votes+=1
    choice.save()
    return redirect('result',question_id)

def result(request,question_id):
    questions = Question.objects.get(id=question_id)
    return render(request,'result.html',{'questions':questions})