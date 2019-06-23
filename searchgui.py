#PyQt5 is used for making GUI for taking imput from user
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PyQt5.QtCore import *
#sesearch is the name of file in which python code is written for searching image on google
from sesearch import *
#qtmoder header file is used for making GUI window of modern style
import qtmodern.styles
import qtmodern.windows

#Wjhen search button will be clicked on_click() function will be called
def on_click():
    textboxValue = textbox.text()  #Getting input from search bar i.e. keyword
    search(textboxValue)           #calling search() from file sesearch
    print(textboxValue)

app = QApplication([])                                  #object of QApplication (header PyQt5)
win = QWidget()                                         #object of QWidget (header PyQt5)

label1 = QLabel()                                       #creating a label
label1.setText("Enter Keyword")                         #naming of label
label1.setStyleSheet("font: 30pt Comic Sans MS")        #changing font
label1.setAlignment(Qt.AlignCenter)                     #aligning to center


textbox = QLineEdit()                                   #creating a textbox
textbox.move(200, 20)
textbox.resize(280,40)


button = QPushButton('Search')                          #creating search button
button.move(20, 80)

#adding label button and ttextbox
vbox = QVBoxLayout()
vbox.addWidget(label1)
vbox.addStretch()
vbox.addWidget(textbox)
vbox.addStretch()
vbox.addWidget(button)
vbox.addStretch()
win.setLayout(vbox)


# connect button to function on_click
button.clicked.connect(on_click)

#naming window
win.setWindowTitle("Image Search")

#modern window
qtmodern.styles.dark(app)
mw = qtmodern.windows.ModernWindow(win)
mw.show()


win.show()
app.exec_()