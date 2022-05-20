from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QProgressBar, qApp
from pyqt_resource_helper import PyQtResourceHelper
from pyqt_svg_button import SvgButton


class PipInterfaceWidget(QWidget):
    containsCursor = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__returnToBigModeBtn = SvgButton()
        self.__closeBtn = SvgButton()
        self.__playPauseBtn = SvgButton()
        self.__videoProgressBar = QProgressBar()

    def __initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(300, 200)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.__closeBtn.clicked.connect(qApp.exit)

        self.__playPauseBtn.setCheckable(True)
        self.__playPauseBtn.setChecked(False)
        self.__playPauseBtn.toggled.connect(self.__playPause)
        self.__playPauseBtn.setShortcut('Space')

        self.__videoProgressBar.setTextVisible(False)

        self.__returnToBigModeBtn.setIcon('ico/pip.svg')
        self.__closeBtn.setIcon('ico/close.svg')
        self.__playPauseBtn.setIcon('ico/play.svg')

        PyQtResourceHelper.setStyleSheet([self.__videoProgressBar], ['style/progressbar.css'])

        topWidget = QWidget()

        topLeftLay = QHBoxLayout()
        topLeftLay.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        topLeftLay.addWidget(self.__returnToBigModeBtn)
        topLeftLay.setContentsMargins(2, 2, 2, 0)

        topRightLay = QHBoxLayout()
        topRightLay.setAlignment(Qt.AlignTop | Qt.AlignRight)
        topRightLay.addWidget(self.__closeBtn)
        topRightLay.setContentsMargins(0, 2, 2, 2)

        lay = QHBoxLayout()
        lay.addLayout(topLeftLay)
        lay.addLayout(topRightLay)
        lay.setContentsMargins(0, 0, 0, 0)

        topWidget.setLayout(lay)

        middleWidget = QWidget()
        lay = QHBoxLayout()
        lay.addWidget(self.__playPauseBtn)
        lay.setContentsMargins(2, 0, 2, 0)
        middleWidget.setLayout(lay)

        bottomWidget = QWidget()
        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignBottom)
        lay.addWidget(self.__videoProgressBar)
        lay.setContentsMargins(0, 0, 0, 0)
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(middleWidget)
        lay.addWidget(bottomWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setLayout(lay)
        self.raise_()

    def __playPause(self, f):
        if f:
            self.__playPauseBtn.setIcon('ico/pause.svg')
        else:
            self.__playPauseBtn.setIcon('ico/play.svg')

    def getReturnToBigModeBtn(self):
        return self.__returnToBigModeBtn

    def getPlayPauseBtn(self):
        return self.__playPauseBtn

    def getVideoProgressBar(self):
        return self.__videoProgressBar

    def enterEvent(self, e):
        self.containsCursor.emit(True)
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.containsCursor.emit(False)
        return super().leaveEvent(e)