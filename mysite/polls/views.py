from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ''.join([p.question_text for p in latest_question_list]) 
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Question %s" % question_id)
