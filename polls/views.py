from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404
from .models import Questions, Choice
from django.views import generic


# def index(request):
#     latest_question_list = Questions.objects.order_by("-pub_date")[:3]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)
class IndexView(generic.ListView):
    template_name ="polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Questions.objects.order_by("-pub_date")[:3]


# def detail(request, question_id):
#     try:
#         question = Questions.objects.get(pk=question_id)
#     except Questions.DoesNotExist:
#         raise Http404("Question does not exist.")
#     return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Questions
    template_name = "polls/detail.html"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'poll/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Questions
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = questions.choice_set.get(pk=request.Post["choice"])
    except(Keyerror, Choice.DoesNotExist):
        return render(request, "polls:detail.html",
                      {"questions": "questions", "errormessage": "you didn't pick up any choices."})
    else:
        selected_choice += 1
        selected_choice.save()
        return HttpResponse("You are voting on the question {}".format(question_id))

# Create your views here.
