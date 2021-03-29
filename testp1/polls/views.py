# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Django , this is our very first polls webapp")
def detail(request, question_id):
    return HttpResponse("this is the detail view of the question : %s" % question_id)
def results(request, question_id):
    return HttpResponse("these are the results of the question : %s" % question_id)
def vote(request, question_id):
    return HttpResponse("Vote on  question : %s" % question_id)