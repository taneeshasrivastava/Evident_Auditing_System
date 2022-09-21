from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QStyle,QSlider,QFileDialog,QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPalette,QColor,QFont
from PyQt5.QtMultimedia import QMediaPlayer , QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys
from PyQt5.QtCore import Qt, QUrl
from templateMatching import templateMatching


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EVAS-AI")
        self.setGeometry(350, 150, 700, 500)
        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)
        self.create_inputpart()
        
    def create_inputpart(self):
        self.openbtn = QPushButton("Open Video")
        self.openbtn.clicked.connect(self.open_file1)
        self.inputbtn = QPushButton("Input Template")
        self.inputbtn.clicked.connect(self.open_template)
        self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        self.openbtn1 = QPushButton("Open Video")
        self.openbtn1.clicked.connect(self.open_file)
        self.playbtn = QPushButton("Play")
        self.playbtn.setEnabled(False)
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playbtn.clicked.connect(self.play_video)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        global hbox
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(self.openbtn1)
        hbox.addWidget(self.playbtn)
        hbox.addWidget(self.slider)
        
        self.mediaPlayer.setVideoOutput(videowidget)
        hbox1 = QHBoxLayout()
        hbox1.setContentsMargins(0,0,0,0)
        hbox1.addWidget(self.openbtn)
        hbox1.addWidget(self.inputbtn)
        vbox1 = QVBoxLayout()
        label1 = QLabel("                                       EVAS-AI                                       ")
        label1.setFont(QFont("Sanserif", 20, QFont.Bold))
        label1.setStyleSheet("QLabel { color : white; }")
        vbox1.addWidget(label1)
        vbox1.addLayout(hbox1)
        vbox1.addWidget(videowidget)
        vbox1.addLayout(hbox)
        self.setLayout(vbox1)
        
    def open_file1(self):
        global filename
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "","Video Files (*.mp4 *.avi *.mpg *.mpeg *.mov *.flv *.wmv *.3gp *.3g2 *.mkv *.m4v)")
        if filename != "":
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playbtn.setEnabled(True)
    def open_template(self):
        templatename, _ = QFileDialog.getOpenFileName(self, "Open File", "","Image Files (*.jpg *.jpeg *.png *.bmp *.tiff *.gif)")
        if templatename != "":
            templateMatching(filename,templatename)
        
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "","Video Files (*.mp4 *.avi *.mpg *.mpeg *.mov *.flv *.wmv *.3gp *.3g2 *.mkv *.m4v)")
        if filename != "":
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playbtn.setEnabled(True)
        
    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
            
    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            
    def positionChanged(self, position):
        self.slider.setValue(position)
        
    def durationChanged(self, duration):
        self.slider.setRange(0,duration)
        
        
        
            
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())