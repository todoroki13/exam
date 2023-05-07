import string
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *

# Create your views here.
def confirm(request):
    return render(request, 'Quiz/confirm.html')

def home(request):
    if request.method == 'POST':
        questions=QuesModel.objects.all()
        ques = 0
        correct = 0
        wrong = 0
        truth = []
        answers = []
        for q in questions:
            ques += 1
            if q.ans == request.POST.get(q.question):
                correct += 1
                truth.append(1)
            else:
                wrong += 1
                truth.append(0)
            if(request.POST.get(q.question)==None):
                answers.append("X")
            else:
                answers.append(request.POST.get(q.question))
        grade = int(correct/ques * 100)

        context = {
            'questions':questions,
            'ques':ques,
            'correct':correct,
            'wrong':wrong,
            'grade':grade,
            'answers':answers,
            'truth':truth,
            'time': request.POST.get('timer'),
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)

def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/home/')
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('home/')

class deleteQuestion(LoginRequiredMixin, DeleteView):
    model = QuesModel
    pk_url_kwarg = 'id'
    success_url = "/home/"
    
class updateQuestion(LoginRequiredMixin, UpdateView):
    model = QuesModel
    pk_url_kwarg = 'id'
    fields = '__all__'
    success_url = "/home/"
        
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')

