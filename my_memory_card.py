#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QButtonGroup, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QMessageBox
from random import shuffle

app = QApplication([])
window = QWidget()

button1 = QRadioButton('6')

button2 = QRadioButton('3')

button3 = QRadioButton('2')

button4 = QRadioButton('8')


window.i = 0
Poslednee = QMessageBox()
line1 = QHBoxLayout()
line2 = QHBoxLayout()


line1.addWidget(button1, alignment = Qt.AlignCenter)
line1.addWidget(button2, alignment = Qt.AlignCenter)


line2.addWidget(button3, alignment = Qt.AlignCenter)
line2.addWidget(button4, alignment = Qt.AlignCenter)


v_line = QVBoxLayout()

v_line.addLayout(line1)
v_line.addLayout(line2)

RadioGroupBox = QGroupBox()
RadioGroupBox.setLayout(v_line)

vopros = QLabel("Сколько материков на земле?")
knopka = QPushButton("Ответить")

v_line1 = QVBoxLayout()

v_line1.addWidget(vopros, alignment = Qt.AlignCenter)
v_line1.addWidget(RadioGroupBox , alignment = Qt.AlignCenter)
v_line1.addWidget(knopka, alignment = Qt.AlignCenter)

H_line_ = QHBoxLayout()
H_line_1 = QHBoxLayout()
H_line_2 = QHBoxLayout()

vopros = QLabel("Сколько материков на земле?")
GroupBox_Pravilniy = QGroupBox("Правильно")
GroupBox_Nepravilniy = QGroupBox("Неправильно")
knopka = QPushButton("Ответить")

H_line_.addWidget(vopros, alignment = Qt.AlignCenter)
H_line_1.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
H_line_1.addWidget(GroupBox_Pravilniy, alignment = Qt.AlignCenter)
H_line_1.addWidget(GroupBox_Nepravilniy, alignment = Qt.AlignCenter)
H_line_2.addWidget(knopka, alignment = Qt.AlignCenter)

v_line_1 = QVBoxLayout()
v_line_1.addLayout(H_line_)
v_line_1.addLayout(H_line_1)
v_line_1.addLayout(H_line_2)


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
question_list.append(Question('Сколько материков на земле?', '6','3','2','8'))
question_list.append(Question('Какой язык Германии?','Немецкий','Испанский','Белорусский', 'Армянский'))


RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)

def show_question():
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)
    RadioGroupBox.show()
    GroupBox_Nepravilniy.hide()
    GroupBox_Pravilniy.hide()
    knopka.setText('Ответить')


spisok = [button1, button2, button3, button4]

def ask(q: Question):
    shuffle(spisok)
    spisok[0].setText(q.right_answer)
    spisok[1].setText(q.wrong1)
    spisok[2].setText(q.wrong2)
    spisok[3].setText(q.wrong3)
    vopros.setText(q.question)
    show_question()



def check_answer():
    if spisok[0].isChecked():
        RadioGroupBox.hide()
        GroupBox_Nepravilniy.hide()
        GroupBox_Pravilniy.show()
        knopka.setText('Следующий вопрос')
        window.i = window.i + 1
    else:
        if spisok[1].isChecked() or spisok[2].isChecked() or spisok[3].isChecked():
            RadioGroupBox.hide()
            GroupBox_Pravilniy.hide()
            GroupBox_Nepravilniy.show()
            knopka.setText("Следующий вопрос")



def next_question():
    window.count = window.count + 1
    if window.count >= len(question_list):
        Poslednee = QMessageBox()
        Poslednee.setText("Правильных ответов:" + str (window.i))
        Poslednee.exec_()
    q = question_list[window.count]
    ask(q)

def click_OK():
    if knopka.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.count = -1

knopka.clicked.connect(click_OK)
next_question()


window.setWindowTitle("Memory Card")
window.resize(400,200)
window.setLayout(v_line_1)
window.show()
app.exec_()


