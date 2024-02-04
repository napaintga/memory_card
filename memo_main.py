from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from memo_app import app
from memo_data import *
from memo_card_layout import *
from memo_main_layout import *


main_width, main_height = 1000, 450 
card_width, card_height = 600, 500 


win_main.show()
app.exec_()