# Generated by Django 3.2 on 2021-06-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0014_question_quiz_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
