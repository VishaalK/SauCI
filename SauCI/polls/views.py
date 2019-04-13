from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = { 'question' : question }
    return render(request, 'polls/detail.html', context)
    # What is idiomatic string interpolation in Python? Compare it to C++
    # At the very least, we know one now. How do different types work, and multiple arguments?

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
