from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from .models import Quiz, Question, Choice
from quiz.dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO


def home(request):
    quiz_names = Quiz.objects.all()
    #print(f'this is{request.__dict__}')
    print(len(request.GET))
    return render(request, 'quiz/home.html', {'quiz_names': quiz_names})


def questions_view(request, category, number = 0):
    print(request.GET)
    number+=1
    questions_list = Question.objects.all().filter(quiz_id = f'{category}', id = f'{category}-{number}')
    choices_list = Choice.objects.all().filter(question_id = f'{category}')

    return render(request, 'quiz/questions.html', {'questions_list':questions_list, 'choices_list':choices_list})








'''def quiz_view(request):
    return render(request, 'base.html')


class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/home.html'
    context_object_name = 'quiz_list'


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'base.html'
    context_object_name = 'quiz'
'''
