from django.shortcuts import render, get_object_or_404,get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Question, Choice

def index(request):
    recent_questions=get_list_or_404(Question.objects.order_by('-pub_date')[:5])
    return render(request, 'mypolls/index.html', {'recent_questions': recent_questions})


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mypolls/details.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'mypolls/details', {
            'question': question,
            'error_message': 'No contestado'
        })
    else:
        return HttpResponseRedirect(reverse('mypolls:results', args=(question_id, )))
        
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'mypolls/results.html', {'question': question})