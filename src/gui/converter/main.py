# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt, QSettings, QTextCodec, QVariant
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QFrame,
        QLabel, QMainWindow, QMenu, QMessageBox, QSizePolicy, QVBoxLayout,
        QWidget, qApp)

import config
from util import load_ini


class LinneConverter(QMainWindow):

    def __init__(self):
        super(LinneConverter, self).__init__()
        self.initUI()

    def initUI(self):
        self.loadSettings()

        last_geo = self.cfg.value('window/geometry')
        if last_geo is None:
            self.setGeometry(*config.DEFAULT_WINDOW_GEO)
        else:
            self.restoreGeometry(last_geo)

        self.setWindowTitle('LinNe Converter')
        self.statusBar().showMessage('Ready')

        self.loadSettings()

        self.createActions()
        #self.createToolbar()
        self.createMenus()
        self.show()

    def loadSettings(self):
        ## load .ini and setup default value
        self.cfg = load_ini(config.SETTING_FILE_PATH)
        self.cfg.setValue('global/version', config.VERSION)


    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(QAction("&New", self, shortcut=QKeySequence.New, statusTip="Create a new file", triggered=self.close))
        self.fileMenu.addSeparator()

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addSeparator()


    def createToolbar(self):
        exitAction = QAction(QIcon('img/icon/exit_24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)


    def createActions(self):
        self.actions = type('myQtAction', (), {})()
        self.actions.exit = QAction("E&xit", self, shortcut="Ctrl+Q", statusTip="Exit the application", triggered=self.close)


    def closeEvent(self, event):
        ## save window position
        self.cfg.setValue('window/geometry', self.saveGeometry())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lc = LinneConverter()
    sys.exit(app.exec_())

