from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSpinBox, QLabel, QRadioButton, QButtonGroup, QHBoxLayout, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt
app = QApplication([])



#ГОЛОВНА ЛІНІЯ ІЗ ВСІМА ВІДЖИТАМИ
main_line = QVBoxLayout()

################
# верхня полоска # створення віджетів
btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")
spin_sleep = QSpinBox()
spin_sleep.setValue(30)
lb_sleep = QLabel("хвилин")
top_list = [btn_sleep, spin_sleep, lb_sleep]


# відображення
top_line = QHBoxLayout()
top_line.addWidget(btn_menu,alignment=Qt.AlignLeft,stretch=60)
top_line.addStretch(1) 
for widget in top_list:
    top_line.addWidget(widget,alignment= Qt.AlignRight)
main_line.addLayout(top_line,stretch=1)
##########



######-------######
#наше питання

lb_question= QLabel("Перекласти слова Мишка")
layout_qtn = QVBoxLayout()
layout_qtn.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
main_line.addLayout(layout_qtn,stretch=2)
#####-------#########

##############
# поле із відповідями
main_layout_ans = QHBoxLayout()
RadioGroupBox = QGroupBox("Варіанти")
RadioGroup = QButtonGroup()

btn_1 = QRadioButton("")
btn_2 = QRadioButton("")
btn_3 = QRadioButton("")
btn_4 = QRadioButton("")

RadioGroup.addButton(btn_1)
RadioGroup.addButton(btn_2)
RadioGroup.addButton(btn_3)
RadioGroup.addButton(btn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(btn_1)
layout_ans2.addWidget(btn_2)
layout_ans3.addWidget(btn_3)
layout_ans3.addWidget(btn_4)
layout_ans1.addLayout(layout_ans3)
layout_ans1.addLayout(layout_ans2)

RadioGroupBox.setLayout(layout_ans1)

######-########
AnsGroupBox = QGroupBox("Результати тесту")
lb_result = QLabel("")
lb_correct = QLabel("")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
#####-#####

main_layout_ans.addWidget(RadioGroupBox)
main_layout_ans.addWidget(AnsGroupBox)

main_line.addLayout(main_layout_ans,stretch=6)
main_line.addStretch(1)
############





####+++++++===#
btn_OK = QPushButton("Відповісти")
layout_ok = QHBoxLayout()
layout_ok.addStretch(1)
layout_ok.addWidget(btn_OK,stretch=2)
layout_ok.addStretch(1)

main_line.addLayout(layout_ok)
main_line.addStretch(1)

####+++++++===#

main_line.setSpacing(1) 
