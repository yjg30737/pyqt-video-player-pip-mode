from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QProgressBar, qApp
from pyqt_resource_helper import PyQtResourceHelper
from pyqt_svg_icon_pushbutton import SvgIconPushButton


class PipInterfaceWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__returnToBigModeBtn = SvgIconPushButton()
        self.__closeBtn = QPushButton('🗙')
        self.__playPauseBtn = QPushButton('⏸')
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

        PyQtResourceHelper.setStyleSheet([self.__returnToBigModeBtn, self.__closeBtn, self.__playPauseBtn], ['style/button.css'])
        self.__closeBtn.setIcon('ico/pip.svg')

        self.__returnToBigModeBtn.setMaximumSize(self.__returnToBigModeBtn.sizeHint())
        self.__closeBtn.setMaximumSize(self.__closeBtn.sizeHint())

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
            self.__playPauseBtn.setText('⏵')
        else:
            self.__playPauseBtn.setText('⏸')

    def getReturnToBigModeBtn(self):
        return self.__returnToBigModeBtn

    def getPlayPauseBtn(self):
        return self.__playPauseBtn

    def getVideoProgressBar(self):
        return self.__videoProgressBar