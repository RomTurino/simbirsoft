# Generated by Django 3.2 on 2021-06-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0008_auto_20210605_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'Список ответов', 'verbose_name_plural': 'Списки ответов'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Вариант', 'verbose_name_plural': 'Варианты'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Викторина', 'verbose_name_plural': 'Викторины'},
        ),
        migrations.AlterField(
            model_name='answers',
            name='id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
