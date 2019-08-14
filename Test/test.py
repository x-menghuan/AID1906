from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        btn = QtWidgets.QPushButton("测试", self)
        btn.move(100, 50)
        btn.clicked.connect(self.test)

        self.setGeometry(200, 100, 800, 600)

    def test(self):
        messagebox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "Title", "Content",
                                           QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        print(messagebox.exec_())


app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()

sys.exit(app.exec_())
