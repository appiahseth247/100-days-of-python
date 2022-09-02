"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 17 - Quiz Game                                                                                    *
*    Subject:  More on OOP: Creating classes with attributes and methods                                    *
*    Date: 2022-04-12                                                                                       *
*************************************************************************************************************
"""

from Day_17_QuizGame_question_model import Question
from Day_17_QuizGame_data import question_data, question_data1
from Day_17_QuizGame_brain import QuizBrain


question_bank = []
position = 0
for question in question_data1:
    # n_question = Question(question["text"], question["answer"])
    question_bank.append(question)
    position += 1

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz! ")
print(f"You final score is : {quiz_brain.scores}/{quiz_brain.question_number}")
