from PyQt5.QtWidgets import (QWidget, QLabel, QToolButton, QHBoxLayout, QLineEdit, QApplication)
from PyQt5 import QtCore
import Network


class WindowHead(QWidget):
    got_network_music_url = QtCore.pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(WindowHead, self).__init__(parent)

#        self.lab_frame = QLabel()
        self.__labWindowLogo = QLabel()
        self.__labWindowLogo.setFixedSize(30, 30)
        self.__labWindowLogo.setStyleSheet('border-image: url(Images/logo);')

        self.__lab_window_title = QLabel('<html><font color="yellow" size=4>大黄狗播放器 汪~汪~</font></html>')

        # 搜索框
        self.search_frame = QWidget()
        self.search_frame.setFixedSize(150, 18)
        self.ln_search = QLineEdit(self.search_frame)
        self.ln_search.setFixedSize(self.search_frame.size())
        self.ln_search.setPlaceholderText('输入歌曲名')
        self.tbn_search = QToolButton(self.search_frame)
        self.tbn_search.setGeometry(128, 2, 15, 15)

        self.__tbnCloseWindow = QToolButton()
        self.__tbnMiniWindow = QToolButton()
        self.__tbnSetting = QToolButton()

        self.__tbnCloseWindow.setFixedSize(11, 11)
        self.__tbnMiniWindow.setFixedSize(11, 11)
        self.__tbnSetting.setFixedSize(11, 11)

        self.setObjectName('lab_frame')
        self.ln_search.setObjectName('ln_search')
        self.tbn_search.setObjectName('tbn_search')
        self.__tbnCloseWindow.setObjectName('closeWindow')
        self.__tbnMiniWindow.setObjectName('miniWindow')
        self.__tbnSetting.setObjectName('setting')

        self.setStyleSheet('''
            #lab_frame{background: rgba(0, 0, 0, 120);}
            #ln_search{
                border: 1px; white;
                border-radius: 9px;
                height: 18px;
            }
            #tbn_search{
                border-image: url(Images/search.png);
            }
            #closeWindow{border-image: url(Images/closeWindow);}
            #closeWindow:hover{border-image: url(Images/closeWindow_hover);}
            #miniWindow{border-image: url(Images/miniWindow);}
            #miniWindow:hover{border-image: url(Images/miniWindow_hover);}
            #setting{border-image: url(Images/setting);}
            #setting:hover{border-image: url(Images/setting_hover);}
            ''')

        self.__layout = QHBoxLayout()
        self.__layout.addWidget(self.__labWindowLogo)
        self.__layout.addStretch(5)
        self.__layout.addWidget(self.__lab_window_title)
        self.__layout.addStretch(1)
        self.__layout.addWidget(self.search_frame)
        self.__layout.addStretch(1)
        self.__layout.addWidget(self.__tbnSetting)
        self.__layout.addWidget(self.__tbnMiniWindow)
        self.__layout.addWidget(self.__tbnCloseWindow)
        self.__layout.setSpacing(10)
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.__layout)

        self.network = Network.NetWork()

        self.__tbnCloseWindow.clicked.connect(self.parentWidget().close)
        self.__tbnMiniWindow.clicked.connect(self.parentWidget().showMinimized)
        self.tbn_search.clicked.connect(self.get_music_play_url)

    def get_music_play_url(self):
        music_name = self.ln_search.text()
        music_url_play_url = self.network.get_music_play_url(music_name)
        self.got_network_music_url.emit(music_name, music_url_play_url)
        print(music_url_play_url)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget = WindowHead()
    widget.show()
    sys.exit(app.exec_())
