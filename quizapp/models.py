import uuid

from django.db import models
from django.urls import reverse

from quiz.dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO


class Choice(models.Model):
    '''which_question: QuestionDTO.uuid = models.ForeignKey(Question, blank=True,
                                                         default=None, on_delete=models.CASCADE)'''
    id: ChoiceDTO.uuid = models.SlugField(max_length=6, primary_key=True)
    question_id: QuestionDTO.uuid = models.PositiveIntegerField(default=1)
    text: ChoiceDTO.text = models.TextField()
    is_correct: ChoiceDTO.is_correct = models.BooleanField(db_index=True)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return f'{self.question_id}-{self.id}. {self.text}'


class Question(models.Model):  # вопрос
    id: QuestionDTO.uuid = models.SlugField(max_length=6, unique=True, primary_key=True)
    quiz_id: QuizDTO.uuid = models.PositiveIntegerField(default=1)
    text: QuestionDTO.text = models.TextField()
    choices: QuestionDTO.choices = models.ManyToManyField(Choice)
    '''category: QuizDTO.uuid = models.ForeignKey(Quiz, null=True, blank=True,
                                 default=None, on_delete=models.CASCADE)'''

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.quiz_id}-{self.id}. {self.text}'



class Quiz(models.Model):  # категория вопросов
    id: QuizDTO.uuid = models.SlugField(max_length=6, unique=True, primary_key=True)
    title: QuizDTO.title = models.CharField(max_length=15, unique=True)
    questions: QuizDTO.questions = models.ManyToManyField(Question)

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'

    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('questions', args=[self.id])


class Answer(models.Model):
    '''answers_list: AnswersDTO.quiz_uuid = models.ForeignKey(Answers, null=True, blank=True,
                                                           default=None, on_delete=models.CASCADE)'''
    choice: QuestionDTO.uuid = models.ForeignKey(Question, blank=True,
                                                 default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'{self.choice}'


class Answers(models.Model):
    id: AnswersDTO.quiz_uuid = models.SlugField(max_length=6, unique=True, primary_key=True)
    answers: AnswersDTO.answers = models.ManyToManyField(Answer)

    class Meta:
        verbose_name = 'Список ответов'
        verbose_name_plural = 'Списки ответов'

    def __str__(self):
        return self.id
