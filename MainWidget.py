# coding: utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QHBoxLayout, QVBoxLayout, QGridLayout, QFileDialog)
from PyQt5.Qt import QDir, QIcon
from PyQt5.QtMultimedia import QMediaPlayer
import WindowHead
import MusicList
import PlayControl


class MyMusicMedia(QWidget):
    def __init__(self, parent=None):
        super(MyMusicMedia, self).__init__(parent)
        self.__offset = 0
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.resize(750, 480)
        self.setWindowTitle('音乐播放器')
        self.setWindowIcon(QIcon('C:/Users/Hello/Desktop/icons/icons/web.png'))

        # 背景图片
        self.__background = QLabel()
        self.__background.setObjectName('background')
        self.__background.setStyleSheet('#background{border-image: url(Images/background);}')

        self.__windowHead = WindowHead.WindowHead(self)

        # 播放列表头
        self.__labMusicListHead = QLabel('<html><font size=4 color="white">播放列表</font></html>')

        # 打开音乐文件按钮
        self.__tbnOpenFile = QComboBox()
        self.__tbnOpenFile.addItem('添加音乐')
        self.__tbnOpenFile.addItem('添加目录')
        self.__tbnOpenFile.setFixedWidth(80)
        self.__tbnOpenFile.setFixedHeight(23)
        self.__tbnOpenFile.activated.connect(self.open_file)
        self.__tbnOpenFile.setObjectName('cob_addMusic')
        self.setStyleSheet('''
                #cob_addMusic{
                    background: rgba(0, 0, 0, 100);
                    margin: 0;
                    padding: 0 0 0 8px;
                    border-radius: 3px;
                    color: rgb(200, 255, 255);
                    width: 80px;
                }
                #cob_addMusic QAbstractItemView:item{height: 20px;}
                #cob_addMusic::drop-down{
                    background: rgba(255, 255, 255, 0);
                    border-image: url(Images/cobIcon.png);
                }
        ''')

        # 播放列表
        self.__musicList = MusicList.MusicList()

        # 播放控制按钮
        self.__playControl = PlayControl.PlayControl()
        self.__playControl.setFixedHeight(40)

        # 布局
        self.__layoutMusicListHead = QHBoxLayout()
        self.__layoutMusicListHead.addWidget(self.__labMusicListHead)
#        self.__layoutMusicListHead.addStretch()
        self.__layoutMusicListHead.addWidget(self.__tbnOpenFile)
        self.__layoutMusicListHead.setContentsMargins(0, 0, 0, 0)

        self.__layoutMusicList = QVBoxLayout()
        self.__layoutMusicList.addLayout(self.__layoutMusicListHead)
        self.__layoutMusicList.addWidget(self.__musicList)
        self.__layoutMusicList.setContentsMargins(0, 0, 0, 0)

        self.__layoutContent = QHBoxLayout()
        self.__layoutContent.addLayout(self.__layoutMusicList)
        self.__layoutContent.addStretch()

        self.__layoutTop = QVBoxLayout()
        self.__layoutTop.addWidget(self.__windowHead)
        self.__layoutTop.addLayout(self.__layoutContent)
        self.__layoutTop.addWidget(self.__playControl)
        self.__layoutTop.setSpacing(3)
        self.__layoutTop.setContentsMargins(5, 5, 8, 5)
        self.__background.setLayout(self.__layoutTop)

        self.__layoutBg = QGridLayout()
        self.__layoutBg.addWidget(self.__background, 0, 0, 1, 1)
        self.__layoutBg.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.__layoutBg)

#        self.connect(self.__playControl, QtCore.SIGNAL('PlayVolume()'), self.play_volume)
#        self.connect(self.__playControl, QtCore.SIGNAL('PlayMode()'), self.play_mode)

        self.__playControl.tbn_play_pause.clicked.connect(self.play_pause)
        self.__playControl.tbn_play_previous.clicked.connect(self.__musicList.playlist.previous)
        self.__playControl.tbn_play_next.clicked.connect(self.__musicList.playlist.next)
        self.__windowHead.got_network_music_url.connect(self.__musicList.add_network_music)

    # 鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__offset = event.globalPos() - self.pos()

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.__offset)

    # 打开音乐
    def open_file(self, current_index):
        filenames = []
        file_types = '*mp3 *wma *wav *asf *aac *mp3pro *vqf *flac *ape *mid *ogg' \
                     ' *MP3 *WMA *WAV *ASF *AAC *MP3PRO *VQF *FLAC *APE *MID *OGG'
        if current_index == 0:
            filenames = QFileDialog.getOpenFileNames(self, '选择音乐文件', 'G:/', file_types)[0]
        elif current_index == 1:
            dir_path = QFileDialog.getExistingDirectory(self, '选择音乐文件', 'G:/')
            filenames = ['%s/%s' % (dir_path, file_name) for file_name in QDir(dir_path).entryList() if file_name != '.' and file_name != '..' and file_name.split('.')[-1] in file_types]
        self.__musicList.add_music_item(filenames)

    def play_pause(self):
        if self.__musicList.player.state() == QMediaPlayer.PlayingState:
            self.__musicList.player.pause()
            self.__playControl.set_play_pause_icon('Images/play_play', 'Images/play_play_hover')
        else:
            self.__musicList.player.play()
            self.__playControl.set_play_pause_icon('Images/play_pause', 'Images/play_pause_hover')

    def play_next(self):
        pass

    def play_previous(self):
        pass

    def play_volume(self):
        pass

    def play_mode(self):
        pass
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    widget = MyMusicMedia()
    widget.show()
    sys.exit(app.exec_())
