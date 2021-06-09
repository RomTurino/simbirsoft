from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List
from quizapp.models import *


class QuizResultService:
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    @property
    def answers(self) -> list[AnswerDTO]:#ответы
        return self.answers_dto.answers

    @property
    def questions(self) -> list[QuestionDTO]:#вопросы
        return self.quiz_dto.questions

    def check_quiz_answers_id(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO) -> bool:#проверка соответствия ответов викторине
        return quiz_dto.uuid == answers_dto.quiz_uuid

    def get_one_question(self) -> QuestionDTO:#один вопрос из викторины
        for question in self.questions:
            yield question

    def get_player_choice(self) -> str:#один ответ участника
        for answers in self.answers:
            yield ''.join(answers.choices)


    def correct_answer(self, question: QuestionDTO)->str:#нахождение правильного варианта
        for choice in question.choices:
            if choice.is_correct:
                return choice.uuid

    def get_result(self) -> float:
        # your code here
        result = []
        for answer in self.answers:
            if self.check_quiz_answers_id(self.quiz_dto, self.answers_dto):
                get_question: QuestionDTO = self.get_one_question()
                get_choice: str = self.get_player_choice()
                question = next(get_question)
                choice = next(get_choice)
                if self.correct_answer(question) and choice == self.correct_answer(question):
                    result.append(True)

        return sum(result) / len(result) if len(result) != 0 else 0
