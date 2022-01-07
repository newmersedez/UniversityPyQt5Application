from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.Controller import *
from Utils.Styles import *

class View(QtWidgets.QMainWindow):
    def __init__(self, model, controller):
        super(View, self).__init__()
        self._model = model
        self._controller = controller
        self._controller.setView(self)
        self._width = 1280
        self._height = 768

        self.resize(1280, 768)
        self.setFont(QtGui.QFont('Arial', 15))
        self.setStyleSheet("QWidget { background-color: #606060; }")
        self._configureLayouts()
        self.show()

    def _configureLayouts(self):
        # Main widget and layout
        self.mainWidget = QtWidgets.QWidget()
        self.withTitleLayout = QtWidgets.QVBoxLayout()
        self.mainLayout = QtWidgets.QHBoxLayout()

        # Menu and content layouts
        self.menuLayout = QtWidgets.QVBoxLayout()
        self.contentLayout = QtWidgets.QVBoxLayout()

        # Title
        self.titleLayout = QtWidgets.QHBoxLayout()
        self.title = QtWidgets.QLabel('Электронная зачетная книжка')
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setFont(QtGui.QFont('Arial', 28))
        self.title.setStyleSheet("QLabel { color : white; }")
        self.titleLayout.addWidget(self.title)
        self.titleLayout.setContentsMargins(0, 0, 0, 20)

        self.line = QtWidgets.QFrame()
        self.line.setGeometry(QtCore.QRect(320, 150, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.withTitleLayout.addLayout(self.titleLayout)
        self.withTitleLayout.addWidget(self.line)
        self.withTitleLayout.addLayout(self.mainLayout)

        # Menu layouts
        self.studyInfoLayout = QtWidgets.QVBoxLayout()
        self.menuLayout.addLayout(self.studyInfoLayout)

        # Configure window central widget
        self.mainLayout.addLayout(self.menuLayout)
        self.mainLayout.addLayout(self.contentLayout)
        self.mainWidget.setLayout(self.withTitleLayout)
        self.menuLayout.setContentsMargins(20, 20, 20, 20)
        self.contentLayout.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(self.mainWidget)

        # Configure layouts
        self._configureButtonsLayout()
        self._configureStudentNameLayout()
        self._configureGroupLayout()
        self._configureDegreeLayout()
        self._configureFormOfEducationLayout()
        self._configureSpecialityCodeLayout()
        self._configureSpecialityNameLayout()
        self._configureContentLayout()

    def _configureButtonsLayout(self):
        self.loginLogoutLayout = QtWidgets.QVBoxLayout()
        self.loginButton = QtWidgets.QPushButton('Войти', self)
        self.loginButton.clicked.connect(self._controller.loginButtonClick)
        self.loginButton.setStyleSheet("color: #00B6FF; font-size:14pt;")
        self.loginButton.setFixedSize(300, 40)
        self.logoutButton = QtWidgets.QPushButton('Выйти', self)
        self.logoutButton.clicked.connect(self._controller.logoutButtonClick)
        self.logoutButton.setStyleSheet("color: #00B6FF; font-size:14pt;")
        self.logoutButton.setFixedSize(300, 40)
        self.logoutButton.setEnabled(False)
        self.loginLogoutLayout.addWidget(self.loginButton)
        self.loginLogoutLayout.addWidget(self.logoutButton)
        self.menuLayout.addLayout(self.loginLogoutLayout)

    def _configureStudentNameLayout(self):
        self.lastnameLayout = QtWidgets.QVBoxLayout()
        self.lastname = QtWidgets.QLabel('Тришин')
        self.lastname.setStyleSheet("QLabel { color : white; }")
        self.lastname.setFont(QtGui.QFont('Arial', 20))
        self.lastnameLayout.addWidget(self.lastname)
        self.studyInfoLayout.addLayout(self.lastnameLayout)
        self.lastname.setHidden(True)

        self.nameLayout = QtWidgets.QVBoxLayout()
        self.name = QtWidgets.QLabel('Дмитрий')
        self.name.setStyleSheet("QLabel { color : white; }")
        self.name.setFont(QtGui.QFont('Arial', 20))
        self.nameLayout.addWidget(self.name)
        self.studyInfoLayout.addLayout(self.nameLayout)
        self.name.setHidden(True)

        self.patronymicLayout = QtWidgets.QVBoxLayout()
        self.patronymic = QtWidgets.QLabel('Александрович')
        self.patronymic.setStyleSheet("QLabel { color : white; }")
        self.patronymic.setFont(QtGui.QFont('Arial', 20))
        self.patronymicLayout.addWidget(self.patronymic)
        self.studyInfoLayout.addLayout(self.patronymicLayout)
        self.patronymic.setHidden(True)

    def _configureGroupLayout(self):
        self.groupLayout = QtWidgets.QVBoxLayout()
        self.staticGroupLabel = QtWidgets.QLabel('Группа')
        self.staticGroupLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self.staticGroupLabel.setFont(QtGui.QFont('Arial', 14))
        self.group = QtWidgets.QLabel('М8О-311Б-19')
        self.group.setStyleSheet("QLabel { color : white; }")
        self.group.setFont(QtGui.QFont('Arial', 18))
        self.groupLayout.addWidget(self.staticGroupLabel)
        self.groupLayout.addWidget(self.group)
        self.studyInfoLayout.addLayout(self.groupLayout)
        self.group.setHidden(True)
        self.staticGroupLabel.setHidden(True)

    def _configureDegreeLayout(self):
        self.degreeLayout = QtWidgets.QVBoxLayout()
        self.staticDegreeLabel = QtWidgets.QLabel('Образование')
        self.staticDegreeLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self.staticDegreeLabel.setFont(QtGui.QFont('Arial', 14))
        self.degree = QtWidgets.QLabel('Бакалавриат')
        self.degree.setStyleSheet("QLabel { color : white; }")
        self.degree.setFont(QtGui.QFont('Arial', 18))
        self.degreeLayout.addWidget(self.staticDegreeLabel)
        self.degreeLayout.addWidget(self.degree)
        self.studyInfoLayout.addLayout(self.degreeLayout)
        self.staticDegreeLabel.setHidden(True)
        self.degree.setHidden(True)

    def _configureFormOfEducationLayout(self):
        self.formOfEducationLayout = QtWidgets.QVBoxLayout()
        self.staticFormOfEducationLabel = QtWidgets.QLabel('Форма обучения')
        self.staticFormOfEducationLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self.staticFormOfEducationLabel.setFont(QtGui.QFont('Arial', 14))
        self.formOfEducation = QtWidgets.QLabel('Очная')
        self.formOfEducation.setStyleSheet("QLabel { color : white; }")
        self.formOfEducation.setFont(QtGui.QFont('Arial', 18))
        self.formOfEducationLayout.addWidget(self.staticFormOfEducationLabel)
        self.formOfEducationLayout.addWidget(self.formOfEducation)
        self.studyInfoLayout.addLayout(self.formOfEducationLayout)
        self.staticFormOfEducationLabel.setHidden(True)
        self.formOfEducation.setHidden(True)

    def _configureSpecialityCodeLayout(self):
        self.specialityCodeLayout = QtWidgets.QVBoxLayout()
        self.staticCodeLabel = QtWidgets.QLabel('Код специальности')
        self.staticCodeLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self.staticCodeLabel.setFont(QtGui.QFont('Arial', 14))
        self.specialityCode = QtWidgets.QLabel('02.03.02')
        self.specialityCode.setStyleSheet("QLabel { color : white; }")
        self.specialityCode.setFont(QtGui.QFont('Arial', 18))
        self.specialityCodeLayout.addWidget(self.staticCodeLabel)
        self.specialityCodeLayout.addWidget(self.specialityCode)
        self.studyInfoLayout.addLayout(self.specialityCodeLayout)
        self.staticCodeLabel.setHidden(True)
        self.specialityCode.setHidden(True)

    def _configureSpecialityNameLayout(self):
        self.specialityNameLayout = QtWidgets.QVBoxLayout()
        self.staticSpecialityNameLabel = QtWidgets.QLabel('Направление')
        self.staticSpecialityNameLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self.staticSpecialityNameLabel.setFont(QtGui.QFont('Arial', 14))
        self.specialityName = QtWidgets.QLabel('Фундаментальная информатика и информационные технологии')
        self.specialityName.setWordWrap(True)
        self.specialityName.setFixedSize(300, 100)
        self.specialityName.setStyleSheet("QLabel { color : white; }")
        self.specialityName.setFont(QtGui.QFont('Arial', 18))
        self.specialityNameLayout.addWidget(self.staticSpecialityNameLabel)
        self.specialityNameLayout.addWidget(self.specialityName)
        self.specialityNameLayout.setContentsMargins(0, 0, 0, 20)
        self.studyInfoLayout.addLayout(self.specialityNameLayout)
        self.staticSpecialityNameLabel.setHidden(True)
        self.specialityName.setHidden(True)

    def _configureContentLayout(self):
        self.actionButtonsLayout = QtWidgets.QHBoxLayout()
        self.tableLayout = QtWidgets.QVBoxLayout()

        self.lessonsButton = QtWidgets.QPushButton('Расписание занятий', self)
        self.lessonsButton.clicked.connect(self._controller.lessonsButtonClicked)
        self.lessonsButton.setStyleSheet("color: #00B6FF; font-size:14pt;")
        self.lessonsButton.setFixedSize(200, 40)
        self.lessonsButton.setHidden(True)
        self.examsButton = QtWidgets.QPushButton('Расписание сессии', self)
        self.examsButton.clicked.connect(self._controller.examsButtonClicked)
        self.examsButton.setStyleSheet("color: #00B6FF; font-size:14pt;")
        self.examsButton.setFixedSize(200, 40)
        self.examsButton.setHidden(True)
        self.gradesButton = QtWidgets.QPushButton('Оценки', self)
        self.gradesButton.clicked.connect(self._controller.gradesButtonClicked)
        self.gradesButton.setStyleSheet("color: #00B6FF; font-size:14pt;")
        self.gradesButton.setFixedSize(200, 40)
        self.gradesButton.setHidden(True)
        self.eventsButton = QtWidgets.QPushButton('Мероприятия', self)
        self.eventsButton.clicked.connect(self._controller.eventsButtonClicked)
        self.eventsButton.setStyleSheet("color: #00B6FF; font-size:14pt;")
        self.eventsButton.setFixedSize(200, 40)
        self.eventsButton.setHidden(True)

        self.actionButtonsLayout.addWidget(self.lessonsButton)
        self.actionButtonsLayout.addWidget(self.examsButton)
        self.actionButtonsLayout.addWidget(self.gradesButton)
        self.actionButtonsLayout.addWidget(self.eventsButton)

        self.table = QtWidgets.QTableWidget()
        self.tableLayout.addWidget(self.table)
        # self.table.setStyleSheet("background-color: #404040; color: white; font-size:14pt;")
        self.table.setStyleSheet(TABLE_STYLE)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setHidden(True)

        self.contentLayout.addLayout(self.actionButtonsLayout)
        self.contentLayout.addLayout(self.tableLayout)
