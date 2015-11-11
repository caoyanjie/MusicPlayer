# coding: utf-8
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import (QMediaPlayer, QMediaPlaylist, QMediaContent)
from PyQt5.QtWidgets import (QListWidget, QApplication)


class MusicList(QListWidget):
    def __init__(self):
        super(MusicList, self).__init__()
        self.__musicList = []
        self.setFixedWidth(250)
        self.setFont(QFont('宋体', 10,))
        self.setObjectName('musicList')
        self.setStyleSheet('#musicList{background-color: rgba(0, 0, 0, 120); color: "green";} #musicList:item{height: 25;}')
        self.itemDoubleClicked.connect(self.music_double_clicked)

        # 初始化多媒体播放器和播放列表
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)

    def add_music_item(self, file_names):
        for file in file_names:
            self.addItem(file.split('/')[-1])
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file)))

    def music_double_clicked(self):
        music_list_index = self.currentRow()
        self.music_play(music_list_index)

    def music_play(self, music_list_index):
        self.playlist.setCurrentIndex(music_list_index)
        self.player.play()

    def add_network_music(self, music_name, music_url):
        print(music_name)
        self.addItem(music_name)
        self.playlist.addMedia(QMediaContent(QUrl(music_url)))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    listWidget = MusicList()
    listWidget.show()
    listWidget.addItem(['i love.mp3', 'you hate.mpe'])
    sys.exit(app.exec_())
