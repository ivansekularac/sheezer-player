from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtMultimedia
from services import RapidAPI, Converter
from styles import stylesheet
import urllib.request
import webbrowser

class Ui_MainWindow(object):

    currentSong = {
        'image': None,
        'preview': None,
        'artist': None,
        'title': None
    }    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 450)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.CustomizeWindowHint)
        MainWindow.setWindowFlags(flags)        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(250, 450))
        MainWindow.setMaximumSize(QtCore.QSize(250, 450))     
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(stylesheet)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, -50, 341, 571))
        self.stackedWidget.setObjectName("stackedWidget")
        self.playerPage = QtWidgets.QWidget()
        self.playerPage.setObjectName("playerPage")
        self.playerImage = QtWidgets.QLabel(self.playerPage)
        self.playerImage.setGeometry(QtCore.QRect(10, 60, 251, 251))
        self.playerImage.setText("")
        self.playerImage.setAlignment(QtCore.Qt.AlignCenter)
        self.playerImage.setObjectName("playerImage")
        self.playerNavigation = QtWidgets.QGroupBox(self.playerPage)
        self.playerNavigation.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.playerNavigation.setTitle("")
        self.playerNavigation.setObjectName("playerNavigation")
        self.btnSearch = QtWidgets.QPushButton(self.playerNavigation)
        self.logo = QtWidgets.QLabel(self.playerNavigation)
        self.logo.setGeometry(QtCore.QRect(75, 6, 130, 20))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("assets/logo.jpg"))
        self.logo.setObjectName("logo")
        self.btnClose = QtWidgets.QPushButton(self.playerNavigation)
        self.btnClose.setGeometry(QtCore.QRect(225, 10, 15, 15))
        self.btnClose.setObjectName("btnClose")
        self.btnSearch.setGeometry(QtCore.QRect(10, 0, 45, 31))
        self.btnSearch.setText("")
        self.iconSearch = QtGui.QIcon()
        self.iconSearch.addPixmap(QtGui.QPixmap("assets/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconPause = QtGui.QIcon()
        self.iconPause.addPixmap(QtGui.QPixmap("assets/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(self.iconSearch)
        self.btnSearch.setObjectName("btnSearch")
        self.btnPlay = QtWidgets.QPushButton(self.playerPage)
        self.btnPlay.setGeometry(QtCore.QRect(100, 410, 74, 74))
        self.btnPlay.setText("")
        self.iconPlay = QtGui.QIcon()
        self.iconPlay.addPixmap(QtGui.QPixmap("assets/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(self.iconPlay)
        self.btnPlay.setIconSize(QtCore.QSize(64, 64))
        self.btnPlay.setObjectName("btnPlay")
        self.lblSongName = QtWidgets.QLabel(self.playerPage)
        self.lblSongName.setGeometry(QtCore.QRect(10, 320, 251, 20))
        self.lblSongName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSongName.setObjectName("lblSongName")
        self.lblArtistName = QtWidgets.QLabel(self.playerPage)
        self.lblArtistName.setGeometry(QtCore.QRect(10, 330, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblArtistName.setFont(font)
        self.lblArtistName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblArtistName.setObjectName("lblArtistName")
        self.songProgress = QtWidgets.QProgressBar(self.playerPage)
        self.songProgress.setGeometry(QtCore.QRect(20, 380, 231, 5))
        self.songProgress.setMinimumSize(QtCore.QSize(0, 5))
        self.songProgress.setMaximumSize(QtCore.QSize(16777215, 5))
        self.songProgress.setProperty("value", 0)
        self.songProgress.setTextVisible(False)
        self.songProgress.setObjectName("songProgress")
        self.lblCurrentDuration = QtWidgets.QLabel(self.playerPage)
        self.lblCurrentDuration.setGeometry(QtCore.QRect(20, 390, 47, 13))
        self.lblCurrentDuration.setObjectName("lblCurrentDuration")
        self.lblDuration = QtWidgets.QLabel(self.playerPage)
        self.lblDuration.setGeometry(QtCore.QRect(200, 390, 47, 13))
        self.lblDuration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDuration.setObjectName("lblDuration")
        self.imageOverlayGroup = QtWidgets.QGroupBox(self.playerPage)
        self.imageOverlayGroup.setGeometry(QtCore.QRect(-10, 250, 291, 61))
        self.imageOverlayGroup.setTitle("")
        self.imageOverlayGroup.setObjectName("imageOverlayGroup")
        self.btnYouTube = QtWidgets.QPushButton(self.playerPage)
        self.btnYouTube.setGeometry(QtCore.QRect(185, 425, 42, 42))
        self.btnYouTube.setText("")
        self.iconYT = QtGui.QIcon()
        self.iconYT.addPixmap(QtGui.QPixmap("assets/youtube-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnYouTube.setIcon(self.iconYT)
        self.btnYouTube.setIconSize(QtCore.QSize(32, 32))
        self.btnYouTube.setObjectName("btnYouTube")
        self.stackedWidget.addWidget(self.playerPage)
        self.searchPage = QtWidgets.QWidget()
        self.searchPage.setObjectName("searchPage")
        self.searchNavigation = QtWidgets.QGroupBox(self.searchPage)
        self.searchNavigation.setGeometry(QtCore.QRect(10, 50, 251, 31))
        self.searchNavigation.setTitle("")
        self.searchNavigation.setObjectName("searchNavigation")
        self.btnBack = QtWidgets.QPushButton(self.searchNavigation)
        self.btnBack.setGeometry(QtCore.QRect(10, 0, 41, 31))
        self.btnBack.setText("")
        self.logo2 = QtWidgets.QLabel(self.searchNavigation)
        self.logo2.setGeometry(QtCore.QRect(75, 6, 130, 20))
        self.logo2.setText("")
        self.logo2.setPixmap(QtGui.QPixmap("assets/logo.jpg"))
        self.logo2.setObjectName("logo")
        self.btnClose2 = QtWidgets.QPushButton(self.searchNavigation)
        self.btnClose2.setGeometry(QtCore.QRect(225, 10, 15, 15))
        self.btnClose2.setObjectName("btnClose2")
        self.iconBack = QtGui.QIcon()
        self.iconBack.addPixmap(QtGui.QPixmap("assets/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(self.iconBack)
        self.btnBack.setObjectName("btnBack")
        self.btnSubmitSearch = QtWidgets.QPushButton(self.searchPage)
        self.btnSubmitSearch.setGeometry(QtCore.QRect(200, 90, 51, 31))
        self.btnSubmitSearch.setText("")
        self.btnSubmitSearch.setIcon(self.iconSearch)
        self.btnSubmitSearch.setObjectName("btnSubmitSearch")
        self.listWidget = QtWidgets.QListWidget(self.searchPage)
        self.listWidget.setGeometry(QtCore.QRect(20, 130, 231, 361))
        self.listWidget.setObjectName("listWidget")
        self.searchInput = QtWidgets.QLineEdit(self.searchPage)
        self.searchInput.setGeometry(QtCore.QRect(20, 90, 231, 31))
        self.searchInput.setObjectName("searchInput")
        self.searchInput.setPlaceholderText("Enter song, artist, album...")
        self.searchNavigation.raise_()
        self.listWidget.raise_()
        self.searchInput.raise_()
        self.btnSubmitSearch.raise_()
        self.stackedWidget.addWidget(self.searchPage)
        MainWindow.setCentralWidget(self.centralwidget)  

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button Actions
        self.btnPlay.clicked.connect(self.playPause)
        self.btnSearch.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.btnBack.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.btnSubmitSearch.clicked.connect(self.showSearchResults)
        self.btnClose.clicked.connect(lambda : exit())
        self.btnClose2.clicked.connect(lambda : exit())
        self.btnYouTube.clicked.connect(lambda: self.youtubeSearch(Ui_MainWindow.currentSong['artist'], Ui_MainWindow.currentSong['title']))

        self.listWidget.itemDoubleClicked.connect(self.loadSelectedSong)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "sheezer"))
        self.lblSongName.setText(_translate("MainWindow", "Song not selected"))
        self.lblArtistName.setText(_translate("MainWindow", "N/A"))
        self.lblCurrentDuration.setText(_translate("MainWindow", ""))
        self.lblDuration.setText(_translate("MainWindow", ""))
        self.btnClose.setText(_translate("MainWindow", "x"))
        self.btnClose2.setText(_translate("MainWindow", "x"))
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.currentChanged.connect(self.checkPlayerState)

    def youtubeSearch(self, *args):
        """Method for opening the browser and pass args to youtube query search"""
        keywords = []        
        for k in args:
            if k:
                keywords.append(k.replace(' ','+'))
        query = "+".join(keywords)
        url = "https://www.youtube.com/results?search_query=" + query

        webbrowser.open(url)

    def checkPlayerState(self):
        if not Ui_MainWindow.currentSong['preview']:
            self.btnPlay.setDisabled(True)
            self.btnYouTube.setHidden(True)
        else:
            self.btnPlay.setDisabled(False)
            self.btnYouTube.setHidden(False)

    def loadPlayer(self):
        self.songUrl = QtCore.QUrl(Ui_MainWindow.currentSong['preview'])
        self.playerContent = QtMultimedia.QMediaContent(self.songUrl)
        self.audioPlayer = QtMultimedia.QMediaPlayer()
        self.audioPlayer.setMedia(self.playerContent)
        self.audioPlayer.durationChanged.connect(self.updateDuration)
        self.audioPlayer.positionChanged.connect(self.updatePosition)
        self.audioPlayer.stateChanged.connect(self.stateCheck)


    def stateCheck(self, state):
        if state == 0:
            self.btnPlay.setIcon(self.iconPlay)
            

    def updateDuration(self, duration):
        self.songProgress.setMaximum(duration)

        if duration >= 0:
            self.lblDuration.setText(Converter.hhmmss(duration))

    def updatePosition(self, position):
        if position >= 0:
            self.lblCurrentDuration.setText(Converter.hhmmss(position))

        # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
        self.songProgress.blockSignals(True)
        self.songProgress.setValue(position)
        self.songProgress.blockSignals(False)
            

    def loadSelectedSong(self):
        self.btnPlay.setIcon(self.iconPlay)
        id = self.clickedItem()
        data = RapidAPI.track_call(id)
        Ui_MainWindow.currentSong['image'] = data['album']['cover_medium']
        Ui_MainWindow.currentSong['preview'] = data['preview']
        Ui_MainWindow.currentSong['artist'] = data['artist']['name']
        Ui_MainWindow.currentSong['title'] = data['title_short']
        self.lblArtistName.setText(data['artist']['name'])
        self.lblSongName.setText(data['title_short'])
        self.stackedWidget.setCurrentIndex(0)
        self.loadPlayer()
        self.loadSongCover()
        
        
    def clickedItem(self):
        item = self.listWidget.currentItem()
        return item.data(4)
    
    def searchResults(self):
        if self.searchInput.text():
            return RapidAPI.search(self.searchInput.text())
        else:
            return False
    
    def showSearchResults(self):
        self.listWidget.clear()
        if self.searchResults():
            results = self.searchResults()
            for song in results:                
                concat = song['artist']['name'] + ' - ' + song['title_short']
                item = QtWidgets.QListWidgetItem()               
                item.setText(concat[:35] + "..." if len(concat) > 35 else concat)
                item.setData(4, song['id'])
                item.setIcon(QtGui.QIcon())
                self.listWidget.addItem(item)
        else:
            self.searchInput.setPlaceholderText("Field can't be empty!")

    def loadSongCover(self):
        image = urllib.request.urlopen(Ui_MainWindow.currentSong['image']).read()
        self.songCover = QtGui.QImage()
        self.songCover.loadFromData(image)
        self.playerImage.setPixmap(QtGui.QPixmap(self.songCover))

    def playPause(self):
        if self.audioPlayer.state() == 1:
            self.audioPlayer.pause()
            self.btnPlay.setIcon(self.iconPlay)
        else:            
            self.audioPlayer.play()
            self.btnPlay.setIcon(self.iconPause)

