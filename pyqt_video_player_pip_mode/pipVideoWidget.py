from PyQt5.QtCore import QTimer, Qt, QPoint, QUrl, QRect
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QSizePolicy, QGridLayout

from pyqt_video_player_pip_mode.pipInterfaceWidget import PipInterfaceWidget


class PipVideoWidget(QWidget):
    def __init__(self, video: str):
        super().__init__()
        self.__initVal()
        self.__initUi(video=video)

    def __initVal(self):
        self.__moving = False
        self.__timer_duration = 3000

        self.__interfaceWidget = PipInterfaceWidget()
        self.__returnToBigModeBtn = self.__interfaceWidget.getReturnToBigModeBtn()
        self.__playPauseBtn = self.__interfaceWidget.getPlayPauseBtn()
        self.__playPauseBtn.toggled.connect(self.__playPause)
        self.__videoProgressBar = self.__interfaceWidget.getVideoProgressBar()

        self.__videoWidget = QVideoWidget(self)
        self.__mediaPlayer = QMediaPlayer()

        self.__timer = QTimer()

    def __initUi(self, video: str):
        self.setFixedSize(300, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setMouseTracking(True)

        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        geo = self.geometry()
        geo.moveBottomRight(QPoint(ag.width(), ag.height()))
        self.setGeometry(geo)

        self.__videoWidget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.__videoWidget.setMouseTracking(True)

        self.__interfaceWidget.setVisible(False)
        self.__interfaceWidget.setMouseTracking(True)
        self.__interfaceWidget.containsCursor.connect(self.__setRemainControlWidgetVisible)

        self.__mediaPlayer.positionChanged.connect(self.__updatePosition)
        self.__mediaPlayer.durationChanged.connect(self.__updateDuration)

        mediaContent = QMediaContent(QUrl.fromLocalFile(video))
        self.__mediaPlayer.setMedia(mediaContent)
        self.setMediaPlayer(self.__mediaPlayer)

        self.__timerInit()

        lay = QGridLayout()
        lay.addWidget(self.__videoWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def __timerInit(self):
        self.__timer.setInterval(self.__timer_duration)
        self.__timer.timeout.connect(self.__toggledInterfaceWidget)

    def __timerStart(self):
        self.__interfaceWidget.move(self.pos())
        self.__interfaceWidget.setVisible(True)
        self.__timer.start()

    def enterEvent(self, e):
        self.__timerStart()
        return super().enterEvent(e)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__moving = True
        return super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self.__moving:
            windowHandle = self.windowHandle()
            windowHandle.startSystemMove()
        if self.__timer.isActive():
            self.__timer.setInterval(self.__timer_duration)
        else:
            self.__timerStart()
        return super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        self.__moving = False
        return super().mouseReleaseEvent(e)

    def leaveEvent(self, e):
        x = self.pos().x()
        y = self.pos().y()

        rect = QRect(x, y, self.width(), self.height())
        if rect.contains(self.cursor().pos()):
            pass
        else:
            self.__interfaceWidget.setVisible(False)
        return super().leaveEvent(e)

    def __toggledInterfaceWidget(self):
        self.__timer.stop()
        self.__interfaceWidget.setVisible(False)

    def __setRemainControlWidgetVisible(self, f):
        if f:
            self.__timer.timeout.disconnect()
        else:
            self.__timer.timeout.connect(self.__toggledInterfaceWidget)

    def setMediaPlayer(self, media_player):
        self.__mediaPlayer = media_player
        self.__mediaPlayer.setVideoOutput(self.__videoWidget)
        self.__mediaPlayer.play()

    def __updatePosition(self, pos):
        self.__videoProgressBar.setValue(pos)

    def __updateDuration(self, duration):
        self.__videoProgressBar.setRange(0, duration)

    def __playPause(self, f):
        if f:
            self.__mediaPlayer.pause()
        else:
            self.__mediaPlayer.play()
