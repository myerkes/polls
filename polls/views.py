from polls.models import Question
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the results for question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)