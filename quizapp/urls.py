from django.urls import path
from quizapp.views import home, questions_view
urlpatterns = [
    path('', home, name = 'home'),
    path('<int:category>/',  questions_view, name = 'questions')
]