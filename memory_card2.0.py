from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('memory card')
main_win.resize(500, 300)
statistic = QWidget()
statistic.resize(400, 200)
all_score = 0
user_score = 0
quest_list_num = -1
statistic.hide()



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
    global user_score
    if answers[0].isChecked():
        show_correct('Правильно!')
        user_score += 1
        user_answer.setText(str(user_score))
    else:         
        show_correct('Неверно!')

def next_question():
    global all_score
    all_score += 1    
    global quest_list_num
    quest_list_num += 1   
    if quest_list_num == len(question_list):
        all_question.setText(str(all_score-1))
        user_percent.setText(str(user_score/(all_score-1)*100))
        main_win.hide()
        statistic.show()
    else:
        ask(question_list[quest_list_num])

#Лаяуты главного окна
main_layout = QVBoxLayout()
layouth1 = QHBoxLayout()
layouth2 = QHBoxLayout()
layouth3 = QHBoxLayout()

#Лаяуты окна статистики
main_stats_layout = QHBoxLayout()
stats_layout_V1 = QVBoxLayout()
stats_layout_V2 = QVBoxLayout()

#Основные виджеты
question = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')

#Виджеты статистики
indicator = QLabel('Показатель')
value = QLabel('Значение')
all_quest_text = QLabel('Макс кол-во баллов')
all_question = QLabel('0')
user_quest_text = QLabel('Кол-во баллов')
user_answer = QLabel('0')
percent = QLabel('Процент')
user_percent = QLabel('0')

#Группы вопросов и ответов
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

#Расположение виджетов на основные лаяуты
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

#Расположение виджетов на лаяуты статистики
stats_layout_V1.addWidget(indicator)
stats_layout_V1.addWidget(all_quest_text)
stats_layout_V1.addWidget(user_quest_text)
stats_layout_V1.addWidget(percent)
stats_layout_V2.addWidget(value,alignment=Qt.AlignCenter)
stats_layout_V2.addWidget(all_question,alignment=Qt.AlignCenter)
stats_layout_V2.addWidget(user_answer,alignment=Qt.AlignCenter)
stats_layout_V2.addWidget(user_percent,alignment=Qt.AlignCenter)
main_stats_layout.addLayout(stats_layout_V1)
main_stats_layout.addLayout(stats_layout_V2)
statistic.setLayout(main_stats_layout)

question_list = []

with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(' ')
        q = Question(data[0],data[1],data[2],data[3],data[4])
        question_list.append(q)
        print(question_list)


#question_list.append(q5)
#question_list.append(q6)

button.clicked.connect(start_test)
next_question()

main_win.show()
app.exec_()