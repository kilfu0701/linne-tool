# -*- coding: utf-8 -*-
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QTextCodec


class QmSetting(QSettings):

    def __init__(self, *args, **kwargs):
        super(QmSetting, self).__init__(*args, **kwargs)

"""
    def
    ## settings
    code = QTextCodec.codecForName('utf-8')
    self.settings = QSettings('.tmp/settings.ini', QSettings.IniFormat)
    self.settings.setIniCodec(code)
    self.settings.setValue('data/c1', 'test')
"""


def load_ini(path, encoding='utf-8'):
    code = QTextCodec.codecForName(encoding)
    settings = QSettings(path, QSettings.IniFormat)
    settings.setIniCodec(code)

    return settings

