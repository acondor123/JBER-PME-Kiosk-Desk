import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QKeyEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 500)
        self.keyboardEntry = ""
        self.initUI()

    def initUI(self):
        checkIn = QtWidgets.QPushButton(self)
        checkIn.setText("Check In")
        checkIn.move(100, 100)

        close = QtWidgets.QPushButton(self)
        close.setText("Close")
        close.move(100, 200)


        

    def keyPressEvent(self, event):
        self.keyboardEntry += chr(event.key())
        print(self.keyboardEntry)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
