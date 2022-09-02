class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.scores = 0

    def still_has_questions(self):
        """  Returns True when there are still questions left or returns False """
        if self.question_number < len(self.question_list):
            return True  # It means there are still questions
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]  # index of current question to be asked
        self.question_number += 1  # Increased index by 1 at this point because indexing start at 0 in python.
        # if we don't increase here, the first output will be "Q.0" instead of "Q.1"
        user_answer = input(f"Q.{self.question_number}: {current_question['question']} (True/False): ")
        correct_answer = current_question["correct_answer"]
        self.check_answer(user_answer, correct_answer)  # call check_answer and pass the user's and correct answer to it

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.scores += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}. ")
        print(f"Your current score is: {self.scores}/{self.question_number}.\n")
