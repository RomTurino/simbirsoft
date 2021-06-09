from django.contrib import admin
from .models import Quiz, Question, Answer, Answers, Choice

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Choice)