# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'superAdminBBIjHe.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 500)
        MainWindow.setMinimumSize(QSize(0, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setBaseSize(QSize(0, 500))
        MainWindow.setStyleSheet(u"*\n"
"{\n"
"border:0\n"
"}\n"
"#topBar,#topBar QPushButton\n"
"{\n"
"background:rgba(11, 39, 33)\n"
"}\n"
"#username\n"
"{\n"
"color:rgba(254, 254, 254,0.856);\n"
"padding: 0 15px 0 5px\n"
"}\n"
"#asideBar\n"
"{\n"
"background :rgb(7, 25, 21)\n"
"}\n"
"#asideBar QPushButton\n"
"{\n"
"color:#fefefe;\n"
"padding : 10px;\n"
"background:rgba(11, 39, 33);\n"
"margin-left : 10px;\n"
"margin-right : 10px;\n"
"border-radius : 10px;\n"
"\n"
"}\n"
"#asideBar QLabel\n"
"{\n"
"color :#fefefe;\n"
"margin-top:8px;\n"
"border-bottom: 2px solid rgb(254, 92, 24);\n"
"border-left: 2px solid rgb(254, 92, 24)\n"
"}\n"
"#asideBar QPushButton:hover\n"
"{\n"
"background-color:rgb(254, 92, 24)\n"
"}\n"
"#frame_4 QTreeWidget\n"
"{\n"
"border : 1px solid rgb(11, 39, 33)\n"
"}\n"
"#Professeurs,#Inspecteurs,#DirEcole,#DirEtude\n"
"{\n"
"background-color:rgb(30, 30, 30)\n"
"}\n"
"QTabWidget QLineEdit\n"
"{\n"
"border-radius:15px;\n"
"padding:3px;\n"
"\n"
"}\n"
"#searchInspectBtn,#searchProfBtn\n"
"{\n"
"background:rgb(3, 12, 10);\n"
"bord"
                        "er-radius:15px;\n"
"}\n"
"#searchInspectBtn:hover,#searchProfBtn:hover\n"
"{\n"
"background-color:rgb(254, 92, 24);\n"
"}\n"
"#frame_7,#frame_18\n"
"{\n"
"background:rgba(30, 30, 30);\n"
"padding: 2px 5px;\n"
"border-radius : 8px;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"border:0;\n"
"background-color:rgb(254, 92, 24);\n"
"height:15px;\n"
"margin:0 40px 0 0\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"background:gray;\n"
"min-width:20px\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"background:blue;\n"
"width:16px;\n"
"subcontrol-position: right;\n"
"subcontrol-origin: margin;\n"
"border:2px solid black;\n"
"}\n"
"QScrollBar::sub-line:horizontal{\n"
"background:magenta;\n"
"width:16px;\n"
"subcontrol-position:top right;\n"
"subcontrol-origin:margin;\n"
"border: 2px solid rgb(11, 39, 33);  \n"
"position: absolute;\n"
"right:20px\n"
"}\n"
"QScrollBar::left-arrow:horizontal,QScrollBar::right-arrow:horizontal{\n"
"width:3px;\n"
"height:3px;\n"
"background:pink;\n"
"}\n"
"QScrollBar::add-page:horizontal,QScro"
                        "llBar::sub-page:horizontal{\n"
"background:none\n"
"}\n"
"QTabWidget::pane{\n"
"border-top:2px solid rgb(254, 92, 24)\n"
"}\n"
"QTabWidget::tab-bar{\n"
"left:5px\n"
"}\n"
"QTabBar::tab{\n"
"background:rgba(254, 92, 24,0.4856);\n"
"border: 0.5px solid #C4C4C3;\n"
"border-bottom-color:#C2C7CB;\n"
"min-width:8px;\n"
"padding:8px;\n"
"color : #fefefe;\n"
"border-top-left-radius :8px;\n"
"border-top-right-radius: 8px;\n"
"}\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"background:rgb(254, 92, 24)\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"border-bottom-color:rgb(254, 92, 24)\n"
"}\n"
"QTabBar::tab:!selected{\n"
"margin-top:2px\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"margin-left:-4px;\n"
"margin-right:-4px\n"
"}\n"
"QTabBar::tab:first:selected\n"
"{\n"
"margin-left:0;\n"
"}\n"
"QTabBar::tab:last:selected\n"
"{\n"
"margin-right:0;\n"
"}\n"
"QTabBar::tab:only-one\n"
"{\n"
"margin:0;\n"
"}\n"
"#frame_4\n"
"{\n"
"background:rgb(60, 60, 60)\n"
"}\n"
"\n"
"#inspectInfo QPushButton,#profInfo QPushButton,#dirEcoleInfo "
                        "QPushButton,#dirEtudeInfo QPushButton\n"
"{\n"
"color:#fefefe;\n"
"padding : 10px;\n"
"background:rgb(254, 92, 24);\n"
"margin-left : 10px;\n"
"margin-right : 10px;\n"
"border-radius : 10px;\n"
"}\n"
"#subinfo1,#subinfo2,#subinfo3,#subinfo4\n"
"{\n"
"background:#fefefe;\n"
"padding: 0 10px;\n"
"border-radius: 10px\n"
"}\n"
"#mailInspect,#mailDirEcole,#mailDirEtude,#mailProf\n"
"{\n"
"background:#fefefe;\n"
"padding: 0 15px;\n"
"border-radius:10px\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 55))
        self.topBar.setMaximumSize(QSize(16777215, 55))
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.topBar)
        self.horizontalLayout_14.setSpacing(2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Logo = QLabel(self.topBar)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(55, 55))
        self.Logo.setMaximumSize(QSize(55, 55))
        self.Logo.setPixmap(QPixmap(u":/images/images/Logo_inp-hb-360x406.png"))
        self.Logo.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.Logo, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.compteBtn = QPushButton(self.topBar)
        self.compteBtn.setObjectName(u"compteBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.compteBtn.setIcon(icon)
        self.compteBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.compteBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.username = QLabel(self.topBar)
        self.username.setObjectName(u"username")
        font = QFont()
        font.setPointSize(14)
        self.username.setFont(font)

        self.horizontalLayout_14.addWidget(self.username)


        self.verticalLayout.addWidget(self.topBar)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.asideBar = QFrame(self.frame_2)
        self.asideBar.setObjectName(u"asideBar")
        self.asideBar.setMinimumSize(QSize(185, 0))
        self.asideBar.setMaximumSize(QSize(185, 16777215))
        self.asideBar.setFrameShape(QFrame.StyledPanel)
        self.asideBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.asideBar)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.asideBar)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.profAccount = QPushButton(self.asideBar)
        self.profAccount.setObjectName(u"profAccount")
        font1 = QFont()
        font1.setPointSize(12)
        self.profAccount.setFont(font1)

        self.verticalLayout_2.addWidget(self.profAccount)

        self.inspectAccount = QPushButton(self.asideBar)
        self.inspectAccount.setObjectName(u"inspectAccount")
        self.inspectAccount.setFont(font1)

        self.verticalLayout_2.addWidget(self.inspectAccount)

        self.dirEtudeAccount = QPushButton(self.asideBar)
        self.dirEtudeAccount.setObjectName(u"dirEtudeAccount")
        self.dirEtudeAccount.setFont(font1)

        self.verticalLayout_2.addWidget(self.dirEtudeAccount)

        self.dirEcoleAccount = QPushButton(self.asideBar)
        self.dirEcoleAccount.setObjectName(u"dirEcoleAccount")
        self.dirEcoleAccount.setFont(font1)

        self.verticalLayout_2.addWidget(self.dirEcoleAccount)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.asideBar)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_5)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setFont(font1)
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setIconSize(QSize(24, 24))
        self.tabWidget.setMovable(True)
        self.Inspecteurs = QWidget()
        self.Inspecteurs.setObjectName(u"Inspecteurs")
        self.horizontalLayout_5 = QHBoxLayout(self.Inspecteurs)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.Inspecteurs)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_16)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(4, 8, 0, 0)
        self.frame_7 = QFrame(self.frame_16)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 35))
        self.frame_7.setMaximumSize(QSize(16777215, 35))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.searchInspect = QLineEdit(self.frame_7)
        self.searchInspect.setObjectName(u"searchInspect")
        self.searchInspect.setMaximumSize(QSize(16777215, 30))
        self.searchInspect.setFont(font1)
        self.searchInspect.setMaxLength(17)
        self.searchInspect.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.searchInspect)

        self.searchInspectBtn = QPushButton(self.frame_7)
        self.searchInspectBtn.setObjectName(u"searchInspectBtn")
        self.searchInspectBtn.setMinimumSize(QSize(32, 32))
        self.searchInspectBtn.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchInspectBtn.setIcon(icon1)
        self.searchInspectBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.searchInspectBtn)


        self.verticalLayout_9.addWidget(self.frame_7, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.inspectTreeWidget = QTreeWidget(self.frame_16)
        self.inspectTreeWidget.setObjectName(u"inspectTreeWidget")

        self.verticalLayout_9.addWidget(self.inspectTreeWidget)


        self.horizontalLayout_5.addWidget(self.frame_16)

        self.inspectInfo = QFrame(self.Inspecteurs)
        self.inspectInfo.setObjectName(u"inspectInfo")
        self.inspectInfo.setMinimumSize(QSize(300, 0))
        self.inspectInfo.setMaximumSize(QSize(300, 16777215))
        self.inspectInfo.setFrameShape(QFrame.StyledPanel)
        self.inspectInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.inspectInfo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.inspectInfo)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 8, 0, 0)
        self.photoInspect = QLabel(self.frame_9)
        self.photoInspect.setObjectName(u"photoInspect")
        self.photoInspect.setMinimumSize(QSize(120, 120))
        self.photoInspect.setMaximumSize(QSize(120, 120))
        self.photoInspect.setPixmap(QPixmap(u":/images/images/manager.png"))
        self.photoInspect.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.photoInspect, 0, Qt.AlignHCenter)

        self.mailInspect = QLabel(self.frame_9)
        self.mailInspect.setObjectName(u"mailInspect")
        self.mailInspect.setMinimumSize(QSize(0, 35))
        self.mailInspect.setMaximumSize(QSize(16777215, 35))
        self.mailInspect.setFont(font1)

        self.verticalLayout_5.addWidget(self.mailInspect, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.subinfo1 = QFrame(self.inspectInfo)
        self.subinfo1.setObjectName(u"subinfo1")
        self.subinfo1.setFrameShape(QFrame.StyledPanel)
        self.subinfo1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.subinfo1)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.subinfo1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_30 = QLabel(self.frame_11)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.verticalLayout_22.addWidget(self.label_30)

        self.nomInspect = QLabel(self.frame_11)
        self.nomInspect.setObjectName(u"nomInspect")
        self.nomInspect.setFont(font1)

        self.verticalLayout_22.addWidget(self.nomInspect)


        self.verticalLayout_18.addWidget(self.frame_11)

        self.frame_33 = QFrame(self.subinfo1)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_31 = QLabel(self.frame_33)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.horizontalLayout_23.addWidget(self.label_31)

        self.sexeInspect = QLabel(self.frame_33)
        self.sexeInspect.setObjectName(u"sexeInspect")
        self.sexeInspect.setFont(font1)

        self.horizontalLayout_23.addWidget(self.sexeInspect)


        self.verticalLayout_18.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.subinfo1)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_35 = QLabel(self.frame_35)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label_35)

        self.telInspect = QLabel(self.frame_35)
        self.telInspect.setObjectName(u"telInspect")
        self.telInspect.setFont(font1)

        self.horizontalLayout_21.addWidget(self.telInspect)


        self.verticalLayout_18.addWidget(self.frame_35)

        self.frame_34 = QFrame(self.subinfo1)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_33 = QLabel(self.frame_34)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)

        self.horizontalLayout_22.addWidget(self.label_33)

        self.filiere = QLabel(self.frame_34)
        self.filiere.setObjectName(u"filiere")
        self.filiere.setFont(font1)

        self.horizontalLayout_22.addWidget(self.filiere)


        self.verticalLayout_18.addWidget(self.frame_34)


        self.verticalLayout_6.addWidget(self.subinfo1)

        self.modifInspectInfo = QPushButton(self.inspectInfo)
        self.modifInspectInfo.setObjectName(u"modifInspectInfo")
        self.modifInspectInfo.setFont(font1)

        self.verticalLayout_6.addWidget(self.modifInspectInfo)


        self.horizontalLayout_5.addWidget(self.inspectInfo, 0, Qt.AlignTop)

        self.tabWidget.addTab(self.Inspecteurs, "")
        self.DirEcole = QWidget()
        self.DirEcole.setObjectName(u"DirEcole")
        self.horizontalLayout_11 = QHBoxLayout(self.DirEcole)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.dirEcoleInfo = QFrame(self.DirEcole)
        self.dirEcoleInfo.setObjectName(u"dirEcoleInfo")
        self.dirEcoleInfo.setMinimumSize(QSize(300, 0))
        self.dirEcoleInfo.setMaximumSize(QSize(300, 16777215))
        self.dirEcoleInfo.setFrameShape(QFrame.StyledPanel)
        self.dirEcoleInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.dirEcoleInfo)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.dirEcoleInfo)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_24)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 8, 0, 0)
        self.photoDirEcole = QLabel(self.frame_24)
        self.photoDirEcole.setObjectName(u"photoDirEcole")
        self.photoDirEcole.setMinimumSize(QSize(120, 120))
        self.photoDirEcole.setMaximumSize(QSize(120, 120))
        self.photoDirEcole.setPixmap(QPixmap(u":/images/images/manager.png"))
        self.photoDirEcole.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.photoDirEcole, 0, Qt.AlignHCenter)

        self.mailDirEcole = QLabel(self.frame_24)
        self.mailDirEcole.setObjectName(u"mailDirEcole")
        self.mailDirEcole.setMinimumSize(QSize(0, 35))
        self.mailDirEcole.setMaximumSize(QSize(16777215, 35))
        self.mailDirEcole.setFont(font1)

        self.verticalLayout_14.addWidget(self.mailDirEcole, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.frame_24, 0, Qt.AlignTop)

        self.subinfo2 = QFrame(self.dirEcoleInfo)
        self.subinfo2.setObjectName(u"subinfo2")
        self.subinfo2.setFrameShape(QFrame.StyledPanel)
        self.subinfo2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.subinfo2)
        self.verticalLayout_20.setSpacing(3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.subinfo2)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_39)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_17 = QLabel(self.frame_39)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.verticalLayout_23.addWidget(self.label_17)

        self.nomdirEcole = QLabel(self.frame_39)
        self.nomdirEcole.setObjectName(u"nomdirEcole")
        self.nomdirEcole.setFont(font1)

        self.verticalLayout_23.addWidget(self.nomdirEcole)


        self.verticalLayout_20.addWidget(self.frame_39)

        self.frame_26 = QFrame(self.subinfo2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_19 = QLabel(self.frame_26)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_19)

        self.sexeDirEcole = QLabel(self.frame_26)
        self.sexeDirEcole.setObjectName(u"sexeDirEcole")
        self.sexeDirEcole.setFont(font1)

        self.horizontalLayout_15.addWidget(self.sexeDirEcole)


        self.verticalLayout_20.addWidget(self.frame_26)

        self.frame_30 = QFrame(self.subinfo2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_39 = QLabel(self.frame_30)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_39)

        self.telDirEcole = QLabel(self.frame_30)
        self.telDirEcole.setObjectName(u"telDirEcole")
        self.telDirEcole.setFont(font1)

        self.horizontalLayout_12.addWidget(self.telDirEcole)


        self.verticalLayout_20.addWidget(self.frame_30)


        self.verticalLayout_13.addWidget(self.subinfo2)

        self.pushButton_11 = QPushButton(self.dirEcoleInfo)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font1)

        self.verticalLayout_13.addWidget(self.pushButton_11)


        self.horizontalLayout_11.addWidget(self.dirEcoleInfo, 0, Qt.AlignTop)

        self.tabWidget.addTab(self.DirEcole, "")
        self.Professeurs = QWidget()
        self.Professeurs.setObjectName(u"Professeurs")
        self.horizontalLayout_6 = QHBoxLayout(self.Professeurs)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.Professeurs)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(4, 8, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.searchProf = QLineEdit(self.frame_18)
        self.searchProf.setObjectName(u"searchProf")
        self.searchProf.setMinimumSize(QSize(0, 35))
        self.searchProf.setMaximumSize(QSize(16777215, 35))
        self.searchProf.setFont(font1)
        self.searchProf.setMaxLength(17)
        self.searchProf.setClearButtonEnabled(True)

        self.horizontalLayout_7.addWidget(self.searchProf)

        self.searchProfBtn = QPushButton(self.frame_18)
        self.searchProfBtn.setObjectName(u"searchProfBtn")
        self.searchProfBtn.setMinimumSize(QSize(32, 32))
        self.searchProfBtn.setMaximumSize(QSize(32, 32))
        self.searchProfBtn.setIcon(icon1)
        self.searchProfBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.searchProfBtn)


        self.verticalLayout_10.addWidget(self.frame_18, 0, Qt.AlignHCenter)

        self.profTreeWidget = QTreeWidget(self.frame_17)
        self.profTreeWidget.setObjectName(u"profTreeWidget")

        self.verticalLayout_10.addWidget(self.profTreeWidget)


        self.horizontalLayout_6.addWidget(self.frame_17)

        self.profInfo = QFrame(self.Professeurs)
        self.profInfo.setObjectName(u"profInfo")
        self.profInfo.setMinimumSize(QSize(300, 0))
        self.profInfo.setMaximumSize(QSize(300, 16777215))
        self.profInfo.setFrameShape(QFrame.StyledPanel)
        self.profInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.profInfo)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.profInfo)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 8, 0, 0)
        self.photoProf = QLabel(self.frame_13)
        self.photoProf.setObjectName(u"photoProf")
        self.photoProf.setMinimumSize(QSize(120, 120))
        self.photoProf.setMaximumSize(QSize(120, 120))
        self.photoProf.setPixmap(QPixmap(u":/images/images/manager.png"))
        self.photoProf.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.photoProf, 0, Qt.AlignHCenter)

        self.mailProf = QLabel(self.frame_13)
        self.mailProf.setObjectName(u"mailProf")
        self.mailProf.setMinimumSize(QSize(0, 35))
        self.mailProf.setMaximumSize(QSize(16777215, 35))
        self.mailProf.setFont(font1)

        self.verticalLayout_8.addWidget(self.mailProf, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.subinfo3 = QFrame(self.profInfo)
        self.subinfo3.setObjectName(u"subinfo3")
        self.subinfo3.setFrameShape(QFrame.StyledPanel)
        self.subinfo3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.subinfo3)
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.subinfo3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_11 = QLabel(self.frame_15)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_11)

        self.nomProf = QLabel(self.frame_15)
        self.nomProf.setObjectName(u"nomProf")
        self.nomProf.setFont(font1)

        self.verticalLayout_16.addWidget(self.nomProf)


        self.verticalLayout_17.addWidget(self.frame_15)

        self.frame_31 = QFrame(self.subinfo3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.frame_31)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.sexeProf = QLabel(self.frame_31)
        self.sexeProf.setObjectName(u"sexeProf")
        self.sexeProf.setFont(font1)

        self.horizontalLayout_13.addWidget(self.sexeProf)


        self.verticalLayout_17.addWidget(self.frame_31)

        self.frame_27 = QFrame(self.subinfo3)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFont(font1)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_37 = QLabel(self.frame_27)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_37)

        self.telProf = QLabel(self.frame_27)
        self.telProf.setObjectName(u"telProf")

        self.horizontalLayout_9.addWidget(self.telProf)


        self.verticalLayout_17.addWidget(self.frame_27)

        self.frame_32 = QFrame(self.subinfo3)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_32)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_15 = QLabel(self.frame_32)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_21.addWidget(self.label_15)

        self.Departement = QLabel(self.frame_32)
        self.Departement.setObjectName(u"Departement")
        self.Departement.setFont(font1)

        self.verticalLayout_21.addWidget(self.Departement)


        self.verticalLayout_17.addWidget(self.frame_32)


        self.verticalLayout_7.addWidget(self.subinfo3)

        self.modifInfoProf = QPushButton(self.profInfo)
        self.modifInfoProf.setObjectName(u"modifInfoProf")
        self.modifInfoProf.setFont(font1)

        self.verticalLayout_7.addWidget(self.modifInfoProf)


        self.horizontalLayout_6.addWidget(self.profInfo, 0, Qt.AlignTop)

        self.tabWidget.addTab(self.Professeurs, "")
        self.DirEtude = QWidget()
        self.DirEtude.setObjectName(u"DirEtude")
        self.horizontalLayout_10 = QHBoxLayout(self.DirEtude)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.DirEtude)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_28)
        self.verticalLayout_15.setSpacing(1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(4, 8, 0, 0)
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addWidget(self.frame_29, 0, Qt.AlignHCenter)

        self.dirEcoleTreeWidget = QTreeWidget(self.frame_28)
        self.dirEcoleTreeWidget.setObjectName(u"dirEcoleTreeWidget")

        self.verticalLayout_15.addWidget(self.dirEcoleTreeWidget)


        self.horizontalLayout_10.addWidget(self.frame_28)

        self.dirEtudeInfo = QFrame(self.DirEtude)
        self.dirEtudeInfo.setObjectName(u"dirEtudeInfo")
        self.dirEtudeInfo.setMinimumSize(QSize(300, 0))
        self.dirEtudeInfo.setMaximumSize(QSize(300, 16777215))
        self.dirEtudeInfo.setFrameShape(QFrame.StyledPanel)
        self.dirEtudeInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.dirEtudeInfo)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.dirEtudeInfo)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_20)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 8, 0, 0)
        self.photoDir = QLabel(self.frame_20)
        self.photoDir.setObjectName(u"photoDir")
        self.photoDir.setMinimumSize(QSize(120, 120))
        self.photoDir.setMaximumSize(QSize(120, 120))
        self.photoDir.setPixmap(QPixmap(u":/images/images/manager.png"))
        self.photoDir.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.photoDir, 0, Qt.AlignHCenter)

        self.mailDir = QLabel(self.frame_20)
        self.mailDir.setObjectName(u"mailDir")
        self.mailDir.setMinimumSize(QSize(0, 35))
        self.mailDir.setMaximumSize(QSize(16777215, 35))
        self.mailDir.setFont(font1)

        self.verticalLayout_12.addWidget(self.mailDir, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_20, 0, Qt.AlignTop)

        self.subinfo4 = QFrame(self.dirEtudeInfo)
        self.subinfo4.setObjectName(u"subinfo4")
        self.subinfo4.setFrameShape(QFrame.StyledPanel)
        self.subinfo4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.subinfo4)
        self.verticalLayout_19.setSpacing(3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.subinfo4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_22)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_22 = QLabel(self.frame_22)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.verticalLayout_24.addWidget(self.label_22)

        self.nomDir = QLabel(self.frame_22)
        self.nomDir.setObjectName(u"nomDir")
        self.nomDir.setFont(font1)

        self.verticalLayout_24.addWidget(self.nomDir)


        self.verticalLayout_19.addWidget(self.frame_22)

        self.frame_38 = QFrame(self.subinfo4)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.sexeDir = QLabel(self.frame_38)
        self.sexeDir.setObjectName(u"sexeDir")
        self.sexeDir.setFont(font1)

        self.horizontalLayout_19.addWidget(self.sexeDir)

        self.label_24 = QLabel(self.frame_38)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_24)


        self.verticalLayout_19.addWidget(self.frame_38)

        self.frame_36 = QFrame(self.subinfo4)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_25 = QLabel(self.frame_36)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.horizontalLayout_18.addWidget(self.label_25)

        self.telDir = QLabel(self.frame_36)
        self.telDir.setObjectName(u"telDir")
        self.telDir.setFont(font1)

        self.horizontalLayout_18.addWidget(self.telDir)


        self.verticalLayout_19.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.subinfo4)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_27 = QLabel(self.frame_37)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_27)

        self.parcours = QLabel(self.frame_37)
        self.parcours.setObjectName(u"parcours")
        self.parcours.setFont(font1)

        self.horizontalLayout_17.addWidget(self.parcours)


        self.verticalLayout_19.addWidget(self.frame_37)


        self.verticalLayout_11.addWidget(self.subinfo4)

        self.modifDirInfo = QPushButton(self.dirEtudeInfo)
        self.modifDirInfo.setObjectName(u"modifDirInfo")
        self.modifDirInfo.setFont(font1)

        self.verticalLayout_11.addWidget(self.modifDirInfo)


        self.horizontalLayout_10.addWidget(self.dirEtudeInfo, 0, Qt.AlignTop)

        self.tabWidget.addTab(self.DirEtude, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Logo.setText("")
        self.compteBtn.setText("")
        self.username.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9ation de Compte", None))
        self.profAccount.setText(QCoreApplication.translate("MainWindow", u"professeur", None))
        self.inspectAccount.setText(QCoreApplication.translate("MainWindow", u"Inspecteur", None))
        self.dirEtudeAccount.setText(QCoreApplication.translate("MainWindow", u"Directeur des \u00e9tudes", None))
        self.dirEcoleAccount.setText(QCoreApplication.translate("MainWindow", u"Directeur de l'\u00e9cole", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.searchInspect.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher.....", None))
        self.searchInspectBtn.setText("")
        ___qtreewidgetitem = self.inspectTreeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Fili\u00e8re", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Sexe", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Pr\u00e9nom(s)", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Matricule", None));
        self.photoInspect.setText("")
        self.mailInspect.setText(QCoreApplication.translate("MainWindow", u"Mail utilisateur", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Nom et pr\u00e9no(s) :", None))
        self.nomInspect.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Sexe", None))
        self.sexeInspect.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.telInspect.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Fili\u00e8re :", None))
        self.filiere.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.modifInspectInfo.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inspecteurs), QCoreApplication.translate("MainWindow", u"Inspecteurs", None))
        self.photoDirEcole.setText("")
        self.mailDirEcole.setText(QCoreApplication.translate("MainWindow", u"Mail utilisateur", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Nom et pr\u00e9nom(s) :", None))
        self.nomdirEcole.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Sexe :", None))
        self.sexeDirEcole.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.telDirEcole.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DirEcole), QCoreApplication.translate("MainWindow", u"Directeur de l'\u00e9cole", None))
        self.searchProf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rechercher.....", None))
        self.searchProfBtn.setText("")
        ___qtreewidgetitem1 = self.profTreeWidget.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"D\u00e9partement", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Sexe", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Pr\u00e9nom(s)", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Matricule", None));
        self.photoProf.setText("")
        self.mailProf.setText(QCoreApplication.translate("MainWindow", u"Mail utilisateur", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nom et Pr\u00e9nom(s):", None))
        self.nomProf.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sexe :", None))
        self.sexeProf.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.telProf.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"D\u00e9partement:", None))
        self.Departement.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.modifInfoProf.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Professeurs), QCoreApplication.translate("MainWindow", u"Professeurs", None))
        ___qtreewidgetitem2 = self.dirEcoleTreeWidget.headerItem()
        ___qtreewidgetitem2.setText(4, QCoreApplication.translate("MainWindow", u"Parcours", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"Sexe", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Pr\u00e9nom(s)", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Matricule", None));
        self.photoDir.setText("")
        self.mailDir.setText(QCoreApplication.translate("MainWindow", u"Mail utilisateur", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Nom et pr\u00e9nom(s) :", None))
        self.nomDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.sexeDir.setText(QCoreApplication.translate("MainWindow", u"Sexe :", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Tel :", None))
        self.telDir.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Parcours :", None))
        self.parcours.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.modifDirInfo.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DirEtude), QCoreApplication.translate("MainWindow", u"Directeur(s) des \u00e9tudes", None))
    # retranslateUi

