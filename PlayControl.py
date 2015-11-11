from PyQt5.QtCore import (pyqtSignal, Qt)
from PyQt5.QtWidgets import (QWidget, QToolButton, QHBoxLayout, QVBoxLayout, QSlider)


class PlayControl(QWidget):
    def __init__(self):
        super(PlayControl, self).__init__()
        self.__tbnSize = 20

        self.tbn_play_pause = QToolButton()
        self.tbn_play_pause.setFixedSize(self.__tbnSize, self.__tbnSize)
        self.tbn_play_pause.setShortcut(Qt.Key_Space)
        self.tbn_play_pause.setObjectName('tbn_play_pause')

        self.tbn_play_next = QToolButton()
        self.tbn_play_next.setFixedSize(self.__tbnSize, self.__tbnSize)
        self.tbn_play_next.setObjectName('tbnPlayNext')

        self.tbn_play_previous = QToolButton()
        self.tbn_play_previous.setFixedSize(self.__tbnSize, self.__tbnSize)
        self.tbn_play_previous.setObjectName('tbn_play_previous')

        self.__tbnPlayVolume = QToolButton()
        self.__tbnPlayVolume.setFixedSize(self.__tbnSize, self.__tbnSize)
        self.__tbnPlayVolume.setObjectName('tbnPlayVolume')

        self.__playProcess = QSlider(Qt.Horizontal)
        self.__playProcess.setFixedHeight(10)
#        self.__playProcess.setStyleSheet('border-image: url(Images/play_pause);')

        self.__tbnPlayMode = QToolButton()
        self.__tbnPlayMode.setFixedSize(self.__tbnSize, self.__tbnSize)
        self.__tbnPlayMode.setObjectName('tbnPlayMode')

        self.__layout = QHBoxLayout()
        self.__layout.addWidget(self.tbn_play_previous)
        self.__layout.addWidget(self.tbn_play_pause)
        self.__layout.addWidget(self.tbn_play_next)
        self.__layout.addWidget(self.__tbnPlayVolume)
        self.__layout.addWidget(self.__tbnPlayMode)

        self.__layoutTop = QVBoxLayout()
        self.__layoutTop.addWidget(self.__playProcess)
        self.__layoutTop.addLayout(self.__layout)
        self.setLayout(self.__layoutTop)

        self.setStyleSheet('''
            #tbn_play_pause{border-image: url(Images/play_pause);}
            #tbn_play_pause:hover{border-image: url(Images/play_pause_hover);}
            #tbn_play_previous{border-image: url(Images/play_previous);}
            #tbn_play_previous:hover{border-image: url(Images/play_previous_hover);}
            #tbnPlayNext{border-image: url(Images/play_next);}
            #tbnPlayNext:hover{border-image: url(Images/play_next_hover);}
            #tbnPlayVolume{border-image: url(Images/volume);}
            #tbnPlayVolume:hover{border-image: url(Images/volume_hover);}
            #tbnPlayMode{border-image: url(Images/playModel_sequence);}
            #tbnPlayMode:hover{border-image: url(Images/playModel_sequence_hover);}
        ''')

#        self.connect(self.tbn_play_pause, QtCore.SIGNAL('clicked()'), QtCore.SIGNAL('PlayPause()'))
#        self.connect(self.tbn_play_next, QtCore.SIGNAL('clicked()'), QtCore.SIGNAL('PlayNext()'))
#        self.connect(self.tbn_play_previous, QtCore.SIGNAL('clicked()'), QtCore.SIGNAL('PlayPrevious()'))
#        self.connect(self.__tbnPlayVolume, QtCore.SIGNAL('clicked()'), QtCore.SIGNAL('PlayVolume()'))
#        self.connect(self.__playProcess, QtCore.SIGNAL('valueChanged(int)'), QtCore.SIGNAL('PlayValueChanged(int)'))
#        self.connect(self.__tbnPlayMode, QtCore.SIGNAL('clicked()'), QtCore.SIGNAL('PlayMode()'))

        self.PlayPause = pyqtSignal()
        self.PlayNext = pyqtSignal()
        self.PlayPrevious = pyqtSignal()
        self.PlayVolume = pyqtSignal()
        self.PlayValueChanged = pyqtSignal()
        self.PlayMode = pyqtSignal()
#        self.tbn_play_pause.clicked.connect(self.parentWidget.parentWidget().close)
        self.tbn_play_next.clicked.connect(self.PlayNext)
        self.tbn_play_previous.clicked.connect(self.PlayPrevious)
        self.__tbnPlayVolume.clicked.connect(self.PlayVolume)
        self.__playProcess.valueChanged.connect(self.PlayValueChanged)
        self.__tbnPlayMode.clicked.connect(self.PlayMode)

    def set_play_pause_icon(self, icon_name, icon_hover_name):
        self.tbn_play_pause.setStyleSheet('QToolButton{border-image: url(%s);} QToolButton:hover{border-image: url(%s);}' % (icon_name, icon_hover_name))