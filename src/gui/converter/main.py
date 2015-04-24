import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

#help(QtGui)

class LinneConverter(QtWidgets.QMainWindow):

    def __init__(self):
        self.width = 800
        self.height = 640

        super(LinneConverter, self).__init__()
        self.initUI()

    def initUI(self):               
        self.statusBar().showMessage('Ready')
        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowTitle('LinNe Converter')
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    lc = LinneConverter()
    sys.exit(app.exec_())

