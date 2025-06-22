from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

q_brain = QuizBrain(question_bank)

while q_brain.still_has_questions():
    q_brain.next_question()

print(f"You have completed the quiz\nYour final score is {q_brain.score}/{q_brain.question_number}")
