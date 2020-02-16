stylesheet = """
        QWidget#centralwidget {
            background-color: #fff;            
        }

        QGroupBox#playerNavigation {
            border: none;
        }

        QLabel#playerImage {
            border-radius: 50px;
            
        }

        QGroupBox#playerNavigation,
        QGroupBox#searchNavigation {
            border: none;
        }

        QPushButton#btnBack,
        QPushButton#btnSearch {            
            background-color: transparent;
            margin-top: 5px;            
            border-radius: 5px;
                   
        }
        QPushButton#btnBack:hover,
        QPushButton#btnSearch:hover {
            background-color: #f2f2f2;
            border-radius: 5px;                             
        }

        QLineEdit#searchInput {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding-left: 5px;
            padding-right: 50px;
            font-size: 12px;
            font-weight: 400;
            color: #14103B;
        }

        QLineEdit#searchInput:focus {
            background-color: #f4f4f4;
        }

        QPushButton#btnSubmitSearch  {
            background-color: #fff;
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
            border-top-left-radius: 0px;
            border-bottom-left-radius: 0px;
            border-top: 1px solid #ccc;
            border-right: 1px solid #ccc;
            border-bottom: 1px solid #ccc;
            border-left: none;
        }

        QPushButton#btnSubmitSearch:hover {
            background-color: #eee;
        }

        QListWidget#listWidget {
            border: 1px solid #ccc;
            border-radius: 3px;
            font-size: 11px;            
        }

        QListWidget#listWidget::item {            
            color: rgba(81,74,157,1);
            padding-top: 3px;
            padding-bottom: 3px;
            border-bottom: 1px solid #eee;
        }        

        QListWidget#listWidget::item::hover {            
            background-color: rgba(81,74,157,0.2);
            border-top: 1px solid rgba(81,74,157,0.3);
            border-bottom: 1px solid rgba(81,74,157,0.3);            
        }

        QListWidget#listWidget::item::selected {            
            background-color: rgba(81,74,157,0.2);
            border: none;
        }            

        QGroupBox#playerNavigation {
            border: none;
            background-color: #fff;
        }
        
        QGroupBox#imageOverlayGroup {
            border: none;            
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, x3:0, y3:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgb(255, 255, 255), stop3: rgb(255, 255, 255));     
        }

        QLabel#lblSongName,
        QLabel#lblArtistName {
            color: rgb(81,74,157);
        }

        QPushButton#btnPlay,
        QPushButton#btnYouTube {
            background-color: transparent;
            border: none;
            
        }

        QPushButton#btnYouTube:hover {
            background-color: #f1f1f1;
            border: none;
            border-radius: 20px; 
        }

        QPushButton#btnPlay:hover {
            background-color: #f1f1f1;
            border: none;
            border-radius: 35px;            
        }

        QProgressBar {
            border: 1px solid #f1f1f1;
            border-radius: 5px;            
        }

        QProgressBar::chunk  {
            background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgba(81,74,157,1), stop:1 rgba(219,37,175,1));
        }

        QPushButton#btnClose,
        QPushButton#btnClose2 {
            background-color: rgb(252, 87, 83);
            color: #fff;
            border: none;
            border-radius: 7px;
            font-size: 10px;
            padding-bottom: 3px;            
        }

        QPushButton#btnClose:hover,
        QPushButton#btnClose2:hover {
            background-color: rgb(214, 79, 77);
        }

    """