from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question, Choice
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    """docstring for IndexView."""
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(seft):
        return Question.objects.order_by('pub_date')[:5]
        pass
class DetailView(generic.DetailView):
    """docstring for DetailView."""
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    """docstring forResultsView."""
    model = Question
    template_name = "polls/results.html"
def home(request):
    my_dict = {'content':'Home page'}
    return render(request,'home.html',context = my_dict)
# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question.id)
#     return render(request, 'polls/results.html',{'question':question})
#
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message':"you didn't select a choice.",
        })
    else:
        if selected_choice.votes > 2:
            a = "you choice right anwser"
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # selected_choice.votes += 1
        # selected_choice.save()
