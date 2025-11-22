from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('memory card')
main_win.resize(500, 300)
main_win.total = 0
main_win.score = 0

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question_text = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    question_group.hide()
    answer_group.show()
    button.setText('Следующий вопрос')

def show_question():
    answer_group.hide()
    question_group.show()
    button.setText('Ответить')
    radio_group.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    radio_group.setExclusive(True)
    

def start_test():
    if button.text() == 'Ответить':
        chech_answer()
    else:
        next_question()

def ask(q: Question):
    shuffle(answers)
    question.setText(q.question_text)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    cor_answer.setText(q.right_answer)
    show_question()

def show_correct(res):
    result.setText(res)
    show_result()



def chech_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:         
        show_correct('Неверно!')
    print('Статистика')
    print('-Всего вопросов:',main_win.total)
    print('-Правильных ответов:',main_win.score)
    print('Рейтинг:', (main_win.score / main_win.total * 100))

def next_question(): 
    main_win.total += 1
    cur_question = randint(0, len(question_list)-1)     
    ask(question_list[cur_question])
    print('Статистика')
    print('-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)


main_layout = QVBoxLayout()
layouth1 = QHBoxLayout()
layouth2 = QHBoxLayout()
layouth3 = QHBoxLayout()

question = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')

question_group = QGroupBox('Варианты ответов')
answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Смурфы')
answer3 = QRadioButton('Чулымцы')
answer4 = QRadioButton('Алеуты')

radio_group = QButtonGroup()
radio_group.addButton(answer1)
radio_group.addButton(answer2)
radio_group.addButton(answer3)
radio_group.addButton(answer4)

layouth_ans = QHBoxLayout()
layouth_ans1 = QVBoxLayout()
layouth_ans2 = QVBoxLayout()
layouth_ans1.addWidget(answer1)
layouth_ans1.addWidget(answer2)
layouth_ans2.addWidget(answer3)
layouth_ans2.addWidget(answer4)
layouth_ans.addLayout(layouth_ans1)
layouth_ans.addLayout(layouth_ans2)
question_group.setLayout(layouth_ans)

answer_group = QGroupBox('результат теста')
result = QLabel('Правильно/Неправильно')
cor_answer = QLabel('Правильный ответ')
main_ans_layout = QVBoxLayout()
main_ans_layout.addWidget(result)
main_ans_layout.addWidget(cor_answer, alignment=Qt.AlignCenter)
answer_group.setLayout(main_ans_layout)

answer_group.hide()
layouth1.addWidget(question, alignment= (Qt.AlignVCenter | Qt.AlignHCenter))
layouth2.addWidget(question_group)
layouth2.addWidget(answer_group)
layouth3.addStretch(1)
layouth3.addWidget(button, stretch=2)
layouth3.addStretch(1)

answers = [answer1, answer2, answer3, answer4]


main_layout.addLayout(layouth1, stretch=2)
main_layout.addLayout(layouth2, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(layouth3, stretch=1)
main_layout.addStretch(1)
main_layout.setSpacing(5)
main_win.setLayout(main_layout)


q1 = Question('Выбери перевод слова переменная','variable', 'variation', 'changing', 'variant')
q2 = Question('Государственный язык бразилии','Португальский','Испанский','Английский','Немецкий')
q3 = Question('Какая страна считается эталоном нейтралитета','Швейцария','Россия','Мексика','Япония')
q4 = Question('Самый сложный язык програмированния','Malbolge','C++','Python','LISP')
question_list = []
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
#question_list.append(q5)
#question_list.append(q6)

button.clicked.connect(start_test)
main_win.score = 0
main_win.total = 0
next_question()

main_win.show()
app.exec_()