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
