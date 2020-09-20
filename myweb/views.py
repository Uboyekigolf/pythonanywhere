from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return render(req, 'myweb/index.html')

def Signup(req):
    return render(req, 'myweb/Signup.html')

def Login(req):
    return render(req, 'myweb/Login.html')


def detail(request, question_id):
    return HttpResponse("You're looking at question {question_id")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)