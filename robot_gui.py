from cmath import isclose
from email.charset import QP
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal

from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Video Player") 
 
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
 
        videoWidget = QVideoWidget()
        self.videotag = None
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
 
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
 
        self.error = QLabel()
        self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 
        #openButton = QPushButton("Open Video")   
        #openButton.setToolTip("Open Video File")
        #openButton.setStatusTip("Open Video File")
        #openButton.setFixedHeight(24)
        #openButton.clicked.connect(self.openFile)
 
 
        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)
 
        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)
 
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.error)
        #layout.addWidget(openButton)
 
        # Set widget to contain window contents
        wid.setLayout(layout)

        self.openVideo()
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
 
    def openVideo(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("videos/cansat1.mp4")))
        self.playButton.setEnabled(True)
        self.mediaPlayer.play()
        

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
 
    def exitCall(self):
        sys.exit(app.exec_())
 
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
 
    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged(self, position):
        self.positionSlider.setValue(position)
 
    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
 
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
 
    def handleError(self):
        self.playButton.setEnabled(False)
        self.error.setText("Error: " + self.mediaPlayer.errorString())

class QLabelClickable(QLabel):
    clicked = pyqtSignal()
    def __init__(self, *args):
        QLabel.__init__(self, *args)
   
    def mouseReleaseEvent(self, ev):
        self.clicked.emit()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")

        ## Pantalla de información ##
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #self.label = QtWidgets.QLabel(self.page_1)
        #self.label.setAlignment(QtCore.Qt.AlignCenter)
        #self.label.setObjectName("label")
        #self.label.setStyleSheet('color: black; font: normal 38px "Cooper Black";')
        #self.verticalLayout_2.addWidget(self.label)
        #self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page_1)
        #self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_aviso = QtWidgets.QLabel(self.page_1)

        pixmap_aviso = QtGui.QPixmap("photos/aviso.jpg")
        self.label_aviso.setPixmap(pixmap_aviso)
        self.label_aviso.setScaledContents(True)

        self.label_aviso.setObjectName("label_aviso")
        #self.label_aviso.setWordWrap(True)
        #self.label_aviso.setStyleSheet('color: white; font: normal 28px "Arial"; text-align: center;')
       
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.page_1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('color: white; font: bold 30px "Arial"; text-align: center; border-radius: 6px; padding: 8px 10px; background-color: black; ')
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.label_aviso)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.page_1)

        ## Pantalla Principal ##        
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('color: white; font: bold 36px "Gill Sans MT";')      
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QLabelClickable(self.page_2)
        pixmap_1 = QtGui.QPixmap("photos/cursos_electivos.png")
        self.label_3.setPixmap(pixmap_1)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QLabelClickable(self.page_2)
        pixmap_2 = QtGui.QPixmap("photos/grupos_investigacion.png")      
        self.label_4.setPixmap(pixmap_2)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_5 = QLabelClickable(self.page_2)
        pixmap_3 = QtGui.QPixmap("photos/proyectos_investigacion.png")
        self.label_5.setPixmap(pixmap_3)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)       
        self.pushButton_finish = QtWidgets.QPushButton(self.page_2)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.pushButton_finish.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_finish = QtWidgets.QHBoxLayout()    
        self.horizontalLayout_finish.addWidget(self.pushButton_finish)

        self.verticalLayout_4.addLayout(self.horizontalLayout_finish)
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page_2)

        ## Pantalla de Cursos electivos ##
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet('color: white; font: bold 36px "Gill Sans MT";')
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QLabelClickable(self.page_3)
        pixmap_b = QtGui.QPixmap("photos/cursos/mtr37b.PNG")
        self.label_8.setPixmap(pixmap_b)
        self.label_8.setStyleSheet('border-radius: 10px;') ###----
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_7 = QLabelClickable(self.page_3)
        pixmap_a = QtGui.QPixmap("photos/cursos/mtr37a.PNG")
        self.label_7.setPixmap(pixmap_a)
        self.label_7.setStyleSheet('border-radius: 10px;') ###----
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_9 = QLabelClickable(self.page_3)
        pixmap_c = QtGui.QPixmap("photos/cursos/mtr343.PNG")
        self.label_9.setPixmap(pixmap_c)
        self.label_9.setStyleSheet('border-radius: 10px;') ###----
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QLabelClickable(self.page_3)
        pixmap_d = QtGui.QPixmap("photos/cursos/mtr361.PNG")
        self.label_10.setPixmap(pixmap_d)
        self.label_10.setStyleSheet('border-radius: 10px;') ###----
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)       
        self.pushButton_atrasCursos = QtWidgets.QPushButton(self.page_3)
        self.pushButton_atrasCursos.setObjectName("pushButton_atrasCursos")
        self.pushButton_atrasCursos.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.verticalLayout_5.addWidget(self.pushButton_atrasCursos)
        self.verticalLayout_5.addWidget(self.label_6)
        self.verticalLayout_5.addLayout(self.gridLayout)    
        self.stackedWidget.addWidget(self.page_3)

        ## Pantalla de Grupos de Investigacion ##
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet('color: white; font: bold 36px "Gill Sans MT";')
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_grupo1 = QLabelClickable(self.page_2)
        pixmap_grupo1 = QtGui.QPixmap("photos/grupos/ia_pucp.png")
        self.label_grupo1.setPixmap(pixmap_grupo1)
        self.label_grupo1.setStyleSheet('border-radius: 10px;') ###----
        self.label_grupo1.setScaledContents(True)
        self.label_grupo1.setObjectName("label_grupo1")
        self.horizontalLayout_2.addWidget(self.label_grupo1)
        self.label_grupo2 = QLabelClickable(self.page_2)
        pixmap_grupo2 = QtGui.QPixmap("photos/grupos/gr_pucp.png")
        self.label_grupo2.setPixmap(pixmap_grupo2)
        self.label_grupo2.setScaledContents(True)
        self.label_grupo2.setObjectName("label_grupo2")
        self.horizontalLayout_2.addWidget(self.label_grupo2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.label_grupo3 = QLabelClickable(self.page_2)
        pixmap_grupo3 = QtGui.QPixmap("photos/grupos/git_pucp.png")
        self.label_grupo3.setPixmap(pixmap_grupo3)
        self.label_grupo3.setScaledContents(True)
        self.label_grupo3.setObjectName("label_grupo3")
        self.verticalLayout_12.addWidget(self.label_grupo3)
        self.pushButton_atrasGrupos = QtWidgets.QPushButton(self.page_4)
        self.pushButton_atrasGrupos.setObjectName("pushButton_atrasGrupos")
        self.pushButton_atrasGrupos.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.verticalLayout_6.addWidget(self.pushButton_atrasGrupos)
        self.verticalLayout_6.addWidget(self.label_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_12)
        self.stackedWidget.addWidget(self.page_4)

        ## Pantalla de Proyectos de Investigacion ##
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet('color: white; font: bold 36px "Gill Sans MT";')
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QLabelClickable(self.page_5)
        pixmap_17 = QtGui.QPixmap("photos/proyectos/GRPUCP_AEROESPACIAL.PNG")
        self.label_17.setPixmap(pixmap_17)
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 1, 1, 1)
        self.label_18 = QLabelClickable(self.page_5)
        pixmap_18 = QtGui.QPixmap("photos/proyectos/ROBOTCAMARAN.PNG")
        self.label_18.setPixmap(pixmap_18)
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_19 = QLabelClickable(self.page_5)
        pixmap_19 = QtGui.QPixmap("photos/proyectos/ROBOTTUBERIAS.PNG")
        self.label_19.setPixmap(pixmap_19)
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_20 = QLabelClickable(self.page_5)
        pixmap_20 = QtGui.QPixmap("photos/proyectos/IAPUCP_Proyecto.png")
        self.label_20.setPixmap(pixmap_20)
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 1, 1, 1)      
        self.pushButton_atrasProy = QtWidgets.QPushButton(self.page_5)
        self.pushButton_atrasProy.setObjectName("pushButton_atrasProy")
        self.pushButton_atrasProy.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.verticalLayout_7.addWidget(self.pushButton_atrasProy)
        self.verticalLayout_7.addWidget(self.label_16)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        self.stackedWidget.addWidget(self.page_5)

        ## Pantalla de Curso 1 ##
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_21 = QtWidgets.QLabel(self.page_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")    
        self.label_curso1 = QtWidgets.QLabel(self.page_6)
        pixmap_4 = QtGui.QPixmap("photos/flyers/mtr37a.png")
        self.label_curso1.setPixmap(pixmap_4)
        self.label_curso1.setScaledContents(True)
        self.label_curso1.setObjectName("label_curso1")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('color: black; font: normal 28px "Arial";')      
        self.pushButton_next1 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_next1.setObjectName("pushButton_next1")
        self.pushButton_next1.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_b1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_b1.addWidget(self.pushButton_next1)
        self.horizontalLayout_b1.addWidget(self.pushButton_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_b1)
        self.verticalLayout_8.addWidget(self.label_21)
        self.verticalLayout_8.addWidget(self.label_curso1)
        self.stackedWidget.addWidget(self.page_6)
        #####

        ## Pantalla de Curso 2 ##
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_22 = QtWidgets.QLabel(self.page_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        
        self.label_curso2 = QtWidgets.QLabel(self.page_7)
        pixmap_4 = QtGui.QPixmap("photos/flyers/mtr37b.png")
        self.label_curso2.setPixmap(pixmap_4)
        self.label_curso2.setScaledContents(True)
        self.label_curso2.setObjectName("label_curso2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet('color: black; font: normal 28px "Arial";')      
        self.pushButton_next2 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_next2.setObjectName("pushButton_next2")
        self.pushButton_next2.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_b2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_b2.addWidget(self.pushButton_next2)
        self.horizontalLayout_b2.addWidget(self.pushButton_3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_b2)
        self.verticalLayout_9.addWidget(self.label_22)
        self.verticalLayout_9.addWidget(self.label_curso2)
        self.stackedWidget.addWidget(self.page_7)
        #####

        ## Pantalla de Curso 3 ##
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_8)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_23 = QtWidgets.QLabel(self.page_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")  
        self.label_curso3 = QtWidgets.QLabel(self.page_8)
        pixmap_5 = QtGui.QPixmap("photos/flyers/mtr343.png")
        self.label_curso3.setPixmap(pixmap_5)
        self.label_curso3.setScaledContents(True)
        self.label_curso3.setObjectName("label_curso3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet('color: black; font: normal 28px "Arial";') 
        self.pushButton_next3 = QtWidgets.QPushButton(self.page_8)
        self.pushButton_next3.setObjectName("pushButton_next3")
        self.pushButton_next3.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_b3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_b3.addWidget(self.pushButton_next3)
        self.horizontalLayout_b3.addWidget(self.pushButton_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_b3)
        self.verticalLayout_10.addWidget(self.label_23)
        self.verticalLayout_10.addWidget(self.label_curso3)
        self.stackedWidget.addWidget(self.page_8)
        #####

        ## Pantalla de Curso 4 ##
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_9)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_24 = QtWidgets.QLabel(self.page_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")   
        self.label_curso4 = QtWidgets.QLabel(self.page_9)
        pixmap_6 = QtGui.QPixmap("photos/flyers/mtr361.png")
        self.label_curso4.setPixmap(pixmap_6)
        self.label_curso4.setScaledContents(True)
        self.label_curso4.setObjectName("label_curso4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet('color: black; font: normal 28px "Arial";')  
        self.pushButton_next4 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_next4.setObjectName("pushButton_next4")
        self.pushButton_next4.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_b4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_b4.addWidget(self.pushButton_next4)
        self.horizontalLayout_b4.addWidget(self.pushButton_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_b4)
        self.verticalLayout_11.addWidget(self.label_24)
        self.verticalLayout_11.addWidget(self.label_curso4)
        self.stackedWidget.addWidget(self.page_9)
        #####

        ## Pantalla de Grupo 1 ##
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_25 = QtWidgets.QLabel(self.page_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_info1 = QtWidgets.QLabel(self.page_10)
        pixmap_info1 = QtGui.QPixmap("photos/info/ia_pucp.png")
        self.label_info1.setPixmap(pixmap_info1)
        self.label_info1.setScaledContents(True)
        self.label_info1.setObjectName("label_info1")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.pushButton_next5 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_next5.setObjectName("pushButton_next5")
        self.pushButton_next5.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_b5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_b5.addWidget(self.pushButton_next5)
        self.horizontalLayout_b5.addWidget(self.pushButton_6)
        self.verticalLayout_13.addLayout(self.horizontalLayout_b5)
        self.verticalLayout_13.addWidget(self.label_25)
        self.verticalLayout_13.addWidget(self.label_info1)
        self.stackedWidget.addWidget(self.page_10)
        #####

        ## Pantalla de Grupo 2 ##
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_11)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_26 = QtWidgets.QLabel(self.page_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_info2 = QtWidgets.QLabel(self.page_11)
        pixmap_info2 = QtGui.QPixmap("photos/info/gr_pucp.png")
        self.label_info2.setPixmap(pixmap_info2)
        self.label_info2.setScaledContents(True)
        self.label_info2.setObjectName("label_info2")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.pushButton_next6 = QtWidgets.QPushButton(self.page_11)
        self.pushButton_next6.setObjectName("pushButton_next6")
        self.pushButton_next6.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_b6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_b6.addWidget(self.pushButton_next6)
        self.horizontalLayout_b6.addWidget(self.pushButton_7)
        self.verticalLayout_14.addLayout(self.horizontalLayout_b6)
        self.verticalLayout_14.addWidget(self.label_26)
        self.verticalLayout_14.addWidget(self.label_info2)
        self.stackedWidget.addWidget(self.page_11)
        #####

        ## Pantalla de Grupo 3 ##
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_12)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_27 = QtWidgets.QLabel(self.page_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")     
        self.label_info3 = QtWidgets.QLabel(self.page_12)
        pixmap_info3 = QtGui.QPixmap("photos/info/git_pucp.png")
        self.label_info3.setPixmap(pixmap_info3)
        self.label_info3.setScaledContents(True)
        self.label_info3.setObjectName("label_info3")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet('color: black; font: normal 28px "Arial";')    
        self.pushButton_next7 = QtWidgets.QPushButton(self.page_12)
        self.pushButton_next7.setObjectName("pushButton_next7")
        self.pushButton_next7.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_b7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_b7.addWidget(self.pushButton_next7)
        self.horizontalLayout_b7.addWidget(self.pushButton_8)
        self.verticalLayout_15.addLayout(self.horizontalLayout_b7)
        self.verticalLayout_15.addWidget(self.label_27)
        self.verticalLayout_15.addWidget(self.label_info3)
        self.stackedWidget.addWidget(self.page_12)
        #####

        ## Pantalla de Video1 ##
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.verticalLayout_vid1 = QtWidgets.QVBoxLayout(self.page_13)
        self.verticalLayout_vid1.setObjectName("verticalLayout_vid1")
        self.label_title_vid1 = QtWidgets.QLabel(self.page_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_title_vid1.setSizePolicy(sizePolicy)
        self.label_title_vid1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_vid1.setObjectName("label_title_vid1")
        #self.verticalLayout_8.addWidget(self.label_title_vid1)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("videos/grpucp/cansat_usa.mp4")))
        self.mediaPlayer.setVideoOutput(videoWidget)       
        self.pushButton_vid1 = QtWidgets.QPushButton(self.page_13)
        self.pushButton_vid1.setObjectName("pushButton_vid1")
        self.pushButton_vid1.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.pushButton_next8=QtWidgets.QPushButton(self.page_13)
        self.pushButton_next8.setObjectName("pushButton_next8")
        self.pushButton_next8.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_video1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_video1.addWidget(self.pushButton_next8)
        self.horizontalLayout_video1.addWidget(self.pushButton_vid1)
        self.verticalLayout_vid1.addLayout(self.horizontalLayout_video1)
        self.verticalLayout_vid1.addWidget(videoWidget)
        self.stackedWidget.addWidget(self.page_13)       

        ## Pantalla de Video2 ##
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.verticalLayout_vid2 = QtWidgets.QVBoxLayout(self.page_14)
        self.verticalLayout_vid2.setObjectName("verticalLayout_vid2")
        self.label_title_vid2 = QtWidgets.QLabel(self.page_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title_vid2.sizePolicy().hasHeightForWidth())
        self.label_title_vid2.setSizePolicy(sizePolicy)
        self.label_title_vid2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_vid2.setObjectName("label_title_vid2")
        #self.verticalLayout_8.addWidget(self.label_title_vid1)

        self.mediaPlayer2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget2 = QVideoWidget()
        self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile("videos/tuberias.mp4")))
        self.mediaPlayer2.setVideoOutput(videoWidget2)

        self.pushButton_vid2 = QtWidgets.QPushButton(self.page_14)
        self.pushButton_vid2.setObjectName("pushButton_vid2")
        self.pushButton_vid2.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.pushButton_next9=QtWidgets.QPushButton(self.page_14)
        self.pushButton_next9.setObjectName("pushButton_next9")
        self.pushButton_next9.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_video2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_video2.addWidget(self.pushButton_next9)
        self.horizontalLayout_video2.addWidget(self.pushButton_vid2)       
        self.verticalLayout_vid2.addLayout(self.horizontalLayout_video2)
        self.verticalLayout_vid2.addWidget(videoWidget2)
        self.stackedWidget.addWidget(self.page_14)

        ## Pantalla de Video3 ##
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.verticalLayout_vid3 = QtWidgets.QVBoxLayout(self.page_15)
        self.verticalLayout_vid3.setObjectName("verticalLayout_vid3")
        self.label_title_vid3 = QtWidgets.QLabel(self.page_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title_vid3.sizePolicy().hasHeightForWidth())
        self.label_title_vid3.setSizePolicy(sizePolicy)
        self.label_title_vid3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_vid3.setObjectName("label_title_vid3")
        #self.verticalLayout_8.addWidget(self.label_title_vid1)

        self.mediaPlayer3 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget3 = QVideoWidget()
        self.mediaPlayer3.setMedia(QMediaContent(QUrl.fromLocalFile("videos/catamaran.mp4")))
        self.mediaPlayer3.setVideoOutput(videoWidget3)

        self.pushButton_vid3 = QtWidgets.QPushButton(self.page_15)
        self.pushButton_vid3.setObjectName("pushButton_vid3")
        self.pushButton_vid3.setStyleSheet('color: black; font: normal 28px "Arial";')

        self.pushButton_next10=QtWidgets.QPushButton(self.page_15)
        self.pushButton_next10.setObjectName("pushButton_next10")
        self.pushButton_next10.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_video3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_video3.addWidget(self.pushButton_next10)
        self.horizontalLayout_video3.addWidget(self.pushButton_vid3)
        self.verticalLayout_vid3.addLayout(self.horizontalLayout_video3)
        self.verticalLayout_vid3.addWidget(videoWidget3)
        self.stackedWidget.addWidget(self.page_15)

        ## Pantalla de Video4 ##
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.verticalLayout_vid4 = QtWidgets.QVBoxLayout(self.page_16)
        self.verticalLayout_vid4.setObjectName("verticalLayout_vid4")
        self.label_title_vid4 = QtWidgets.QLabel(self.page_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_title_vid4.setSizePolicy(sizePolicy)
        self.label_title_vid4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_vid4.setObjectName("label_title_vid4")
        #self.verticalLayout_8.addWidget(self.label_title_vid1)

        self.mediaPlayer4 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget4 = QVideoWidget()
        self.mediaPlayer4.setMedia(QMediaContent(QUrl.fromLocalFile("videos/iapucp_proyecto.mp4")))
        self.mediaPlayer4.setVideoOutput(videoWidget4)

        self.pushButton_vid4 = QtWidgets.QPushButton(self.page_16)
        self.pushButton_vid4.setObjectName("pushButton_vid4")
        self.pushButton_vid4.setStyleSheet('color: black; font: normal 28px "Arial";')

        self.pushButton_next11=QtWidgets.QPushButton(self.page_16)
        self.pushButton_next11.setObjectName("pushButton_next11")
        self.pushButton_next11.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_video4 = QtWidgets.QHBoxLayout()   
        self.horizontalLayout_video4.addWidget(self.pushButton_next11)
        self.horizontalLayout_video4.addWidget(self.pushButton_vid4)
        self.verticalLayout_vid4.addLayout(self.horizontalLayout_video4)
        self.verticalLayout_vid4.addWidget(videoWidget4)
        self.stackedWidget.addWidget(self.page_16)


        ##Pantalla QR
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.verticalLayout_qr = QtWidgets.QVBoxLayout(self.page_17)
        self.verticalLayout_qr.setObjectName("verticalLayout_qr")
        self.label_qr = QtWidgets.QLabel(self.page_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)    
        sizePolicy.setHeightForWidth(self.label_qr.sizePolicy().hasHeightForWidth())
        self.label_qr.setSizePolicy(sizePolicy)
        self.label_qr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qr.setObjectName("label_qr")
        self.label_qr.setStyleSheet('color: white; font: bold 36px "Gill Sans MT";')
        
        self.label_qr_2= QtWidgets.QLabel(self.page_17)
        pixmap_qr = QtGui.QPixmap("photos/qr.png")

        self.label_qr_2.setPixmap(pixmap_qr)
        self.label_qr_2.setScaledContents(True)
        self.label_qr_2.setStyleSheet('width: 10px; height: 10px;')

        self.label_qr_2.setAlignment(Qt.AlignCenter)
        self.label_qr_2.setObjectName("label_qr_2")   

        self.pushButton_finish_qr = QtWidgets.QPushButton(self.page_17)
        self.pushButton_finish_qr.setObjectName("pushButton_finish_qr")
        self.pushButton_finish_qr.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.pushButton_back_qr = QtWidgets.QPushButton(self.page_17)
        self.pushButton_back_qr.setObjectName("pushButton_back_qr")
        self.pushButton_back_qr.setStyleSheet('color: black; font: normal 28px "Arial";')
        self.horizontalLayout_qr = QtWidgets.QHBoxLayout()
        self.horizontalLayout_qr.addWidget(self.pushButton_back_qr)
        self.horizontalLayout_qr.addWidget(self.pushButton_finish_qr)
        self.verticalLayout_qr.addLayout(self.horizontalLayout_qr)
        self.verticalLayout_qr.addWidget(self.label_qr)
        self.verticalLayout_qr.addWidget(self.label_qr_2)
        self.stackedWidget.addWidget(self.page_17)
        #####
        ###
        ##


        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encuesta Telemarketing"))
        #self.label.setText(_translate("MainWindow", "ACUERDO DE CONFIDENCIALIDAD"))

        aviso = " ".join(["YO ACEPTO participar en una prueba de deteccion de emociones conducida por el equipo del Robot", 
        "de Telemarketing para la Interaccion Humano Robot, realizada el dia 25/07/2022 en la facultad de",
        "Ingenieria Mecatronica de la Pontificia Universidad Catolica del Peru, ubicada en Av. Universitaria" ,
        "1801 San Miguel, 15088, Lima.\n\nEntiendo y estoy de acuerdo con las condiciones mencionadas en adelante.",
        "\n\nEntiendo que el experimento tiene por objetivo evaluar las reacciones emocionales ante los avisos mostrados,",
        "NO mis capacidades, habilidades o conocimientos. \n\nEntiendo que los resultados del experimento se utilizaran",
        "solo para propositos academicos y/o de investigacion sin que mi identidad sea revelada.",
        "\n\nEntiendo que sere filmado durante el proceso a fin de evaluar mi experiencia y que la filmacion sera destruida",
        "una vez terminado el analisis y jamas sera divulgada.",
        "\n\nEntiendo que puedo comunicar al supervisor del experimento, en cualquier momento, sobre algun malestar,",
        "molestia o inconformidad que pueda sentir durante el desarrollo del experimento; y que, por tal motivo,",
        "puedo abandonar el experimento y el sitio de pruebas en cualquier momento."])

        #self.label_aviso.setText(_translate("MainWindow",aviso))

        self.pushButton.setText(_translate("MainWindow", "ACEPTAR"))
        self.label_2.setText(_translate("MainWindow", "¿Qué te gustaría ver?"))
        #self.label_3.setText(_translate("MainWindow", "Cursos Electivos"))
        #self.label_4.setText(_translate("MainWindow", "Grupos de Investigación"))
        #self.label_5.setText(_translate("MainWindow", "Proyectos de Investigación"))
        self.label_6.setText(_translate("MainWindow", "Cursos electivos"))
        #self.label_8.setText(_translate("MainWindow", "Robótica Avanzada"))
        #self.label_7.setText(_translate("MainWindow", "Topics on Advanced Robotics"))
        #self.label_9.setText(_translate("MainWindow", "TextLabel"))
        #self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "Grupos de Investigación"))
        self.label_16.setText(_translate("MainWindow", "Proyectos de Investigación"))
        #self.label_17.setText(_translate("MainWindow", "GRPUCP - CanSat Competition USA 2022"))
        #self.label_18.setText(_translate("MainWindow", "Proyecto 1"))
        #self.label_19.setText(_translate("MainWindow", "Proyecto 3"))
        #self.label_20.setText(_translate("MainWindow", "Proyecto 4"))
        self.label_qr.setText(_translate("MainWindow", "LINK DE LA ENCUESTA"))

        self.pushButton_next1.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next2.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next3.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next4.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next5.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next6.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next7.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next8.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next9.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next10.setText(_translate("MainWindow", "INICIO"))
        self.pushButton_next11.setText(_translate("MainWindow", "INICIO"))

        self.pushButton_2.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_3.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_4.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_5.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_6.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_7.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_8.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_vid1.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_vid2.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_vid3.setText(_translate("MainWindow", "REGRESAR"))
        self.pushButton_vid4.setText(_translate("MainWindow", "REGRESAR"))
        
        self.pushButton_atrasCursos.setText(_translate("MainWindow","REGRESAR"))
        self.pushButton_atrasGrupos.setText(_translate("MainWindow","REGRESAR"))
        self.pushButton_atrasProy.setText(_translate("MainWindow","REGRESAR"))
        self.pushButton_finish.setText(_translate("MainWindow","TERMINAR"))

        self.pushButton_back_qr.setText(_translate("MainWindow","REGRESAR"))
        self.pushButton_finish_qr.setText(_translate("MainWindow","FINALIZAR"))

        
        self.pushButton.clicked.connect(self.gotoMenu)

        self.label_3.clicked.connect(self.gotoElectivos)
        self.label_4.clicked.connect(self.gotoGruposInvestiga)
        self.label_5.clicked.connect(self.gotoProyectosInvestiga)

        ## Pantalla principal ## --
        self.pushButton_finish.clicked.connect(self.gotoEncuesta)
        ###################### --

        ## Cursos electivos ##
        self.label_7.clicked.connect(self.gotoFlyer1)
        self.label_8.clicked.connect(self.gotoFlyer2)
        self.label_9.clicked.connect(self.gotoFlyer3)
        self.label_10.clicked.connect(self.gotoFlyer4)

        self.pushButton_2.clicked.connect(self.gotoElectivos)
        self.pushButton_3.clicked.connect(self.gotoElectivos)
        self.pushButton_4.clicked.connect(self.gotoElectivos)
        self.pushButton_5.clicked.connect(self.gotoElectivos)
        self.pushButton_atrasCursos.clicked.connect(self.gotoMenu)
        ######################

        ## Grupos de Investigacion ##
        self.label_grupo1.clicked.connect(self.gotoGrupo1)
        self.label_grupo2.clicked.connect(self.gotoGrupo2)
        self.label_grupo3.clicked.connect(self.gotoGrupo3)

        self.pushButton_6.clicked.connect(self.gotoGruposInvestiga)
        self.pushButton_7.clicked.connect(self.gotoGruposInvestiga)
        self.pushButton_8.clicked.connect(self.gotoGruposInvestiga)

        self.pushButton_atrasGrupos.clicked.connect(self.gotoMenu)
        #############################

        ## Proyectos de Investigación ##

        self.pushButton_vid1.clicked.connect(self.gobackProyectos)
        self.label_17.clicked.connect(self.gotoVideo1)

        self.pushButton_vid2.clicked.connect(self.gobackProyectos)
        self.label_18.clicked.connect(self.gotoVideo2)

        self.pushButton_vid3.clicked.connect(self.gobackProyectos)
        self.label_19.clicked.connect(self.gotoVideo3)

        self.pushButton_vid4.clicked.connect(self.gobackProyectos)
        self.label_20.clicked.connect(self.gotoVideo4)

        self.pushButton_atrasProy.clicked.connect(self.gotoMenu)
        ################################

        ##Botones Inicio
        self.pushButton_next1.clicked.connect(self.gotoMenu)
        self.pushButton_next2.clicked.connect(self.gotoMenu)
        self.pushButton_next3.clicked.connect(self.gotoMenu)
        self.pushButton_next4.clicked.connect(self.gotoMenu)
        self.pushButton_next5.clicked.connect(self.gotoMenu)
        self.pushButton_next6.clicked.connect(self.gotoMenu)
        self.pushButton_next7.clicked.connect(self.gotoMenu)
        self.pushButton_next8.clicked.connect(self.gotoMenu)
        self.pushButton_next9.clicked.connect(self.gotoMenu)
        self.pushButton_next10.clicked.connect(self.gotoMenu)
        self.pushButton_next11.clicked.connect(self.gotoMenu)
        self.pushButton_back_qr.clicked.connect(self.gotoMenu)

        self.pushButton_finish_qr.clicked.connect(self.gotoAviso)
        ################################

    ## Funciones principales ##}
    def gotoAviso(self):
        self.stackedWidget.setCurrentIndex(0)

    def gotoElectivos(self):
        self.stackedWidget.setCurrentIndex(2)

    def gotoGruposInvestiga(self):
        self.stackedWidget.setCurrentIndex(3)

    def gotoProyectosInvestiga(self):
        self.stackedWidget.setCurrentIndex(4)

    def gotoMenu(self):
        self.stackedWidget.setCurrentIndex(1)
        self.mediaPlayer.stop()
        self.mediaPlayer2.stop()
        self.mediaPlayer3.stop()
        self.mediaPlayer4.stop()

    def gobackProyectos(self):
        self.stackedWidget.setCurrentIndex(4)
        self.mediaPlayer.stop()
        self.mediaPlayer2.stop()
        self.mediaPlayer3.stop()
        self.mediaPlayer4.stop()

    def goBack(self):
        self.stackedWidget.setCurrentIndex(3)
    ####################################

    ## Funciones para mostrar flyers ##
    def gotoFlyer1(self):
        self.stackedWidget.setCurrentIndex(5)

    def gotoFlyer2(self):
        self.stackedWidget.setCurrentIndex(6)

    def gotoFlyer3(self):
        self.stackedWidget.setCurrentIndex(7)

    def gotoFlyer4(self):
        self.stackedWidget.setCurrentIndex(8)
    ####################################

    ## Funciones para mostrar grupos ##
    def gotoGrupo1(self):
        self.stackedWidget.setCurrentIndex(9)

    def gotoGrupo2(self):
        self.stackedWidget.setCurrentIndex(10)

    def gotoGrupo3(self):
        self.stackedWidget.setCurrentIndex(11)
    ####################################

    # Funciones para mostrar videos #
    def gotoVideo1(self):
        self.stackedWidget.setCurrentIndex(12)
        self.mediaPlayer.play()

    def gotoVideo2(self):
        self.stackedWidget.setCurrentIndex(13)
        self.mediaPlayer2.play()

    def gotoVideo3(self):
        self.stackedWidget.setCurrentIndex(14)
        self.mediaPlayer3.play()

    def gotoVideo4(self):
        self.stackedWidget.setCurrentIndex(15)
        self.mediaPlayer4.play()

    def gotoEncuesta(self):
        self.stackedWidget.setCurrentIndex(16)
    #################################

##Estilo de la imagen en background
stylesheet = """
    QMainWindow {
        background-image: url("photos/fondo.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
""" 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Encuesta Telemarketing")
    MainWindow.setWindowIcon(QtGui.QIcon("photos/icono.png"))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    #MainWindow.show()
    sys.exit(app.exec_())
