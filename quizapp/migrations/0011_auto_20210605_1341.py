# Generated by Django 3.2 on 2021-06-05 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0010_auto_20210605_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='quizapp.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.SlugField(max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
