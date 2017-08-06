from django.shortcuts import render
from django.http import HttpResponse
from .models import question

def index(request):
    latest_question = question.objects.order_by('-pubDate')[:5]
    output = ", ".join(q.questionText for q in latest_question)
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse('Question detail %s' % question_id)


def results(request, question_id):
    return HttpResponse('Question result %s' % question_id)


def vote(request, question_id):
    return HttpResponse('Vote on question %s' % question_id)
