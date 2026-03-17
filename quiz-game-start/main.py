from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    formated_question = Question(question_text, question_answer)
    question_bank.append(formated_question)


quizz = QuizBrain(question_bank)
while quizz.question_remaining():
    quizz.next_question()
    if not quizz.question_remaining():
        print(f"You have reached the end of the quiz \n Your final score is {quizz.score}/{quizz.q_number} ")