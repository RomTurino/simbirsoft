from typing import List, NamedTuple


class ChoiceDTO(NamedTuple):#правильный выбор
    uuid: str#1-1-1
    text: str
    is_correct: bool


class QuestionDTO(NamedTuple):#сам вопрос
    uuid: str#1-1
    text: str
    choices: List[ChoiceDTO]


class QuizDTO(NamedTuple):#возможно, список вопросов
    uuid: str#1
    title: str
    questions: List[QuestionDTO]


class AnswerDTO(NamedTuple):
    question_uuid: str#1-1
    choices: List[str]#1-1-1


class AnswersDTO(NamedTuple):
    quiz_uuid: str#1
    answers: List[AnswerDTO]
