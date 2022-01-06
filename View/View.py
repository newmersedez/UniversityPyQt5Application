from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.Controller import *


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
        self.title = QtWidgets.QLabel('Электронная зачетка МАИ')
        self.title.setFont(QtGui.QFont('Arial', 28))
        self.title.setStyleSheet("QLabel { color : white; }")
        self.titleLayout.addWidget(self.title)
        self.withTitleLayout.addLayout(self.titleLayout)
        self.withTitleLayout.addLayout(self.mainLayout)

        # Buttons
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

        # Menu layouts
        self.studyInfoLayout = QtWidgets.QVBoxLayout()
        self.menuLayout.addLayout(self.studyInfoLayout)

        # Lastname Name Patronymic
        self.lastnameLayout = QtWidgets.QVBoxLayout()
        self.lastname = QtWidgets.QLabel('Тришин')
        self.lastname.setStyleSheet("QLabel { color : white; }")
        self.lastname.setFont(QtGui.QFont('Arial', 25))
        self.lastnameLayout.addWidget(self.lastname)
        self.studyInfoLayout.addLayout(self.lastnameLayout)
        self.lastname.setHidden(True)

        self.nameLayout = QtWidgets.QVBoxLayout()
        self.name = QtWidgets.QLabel('Дмитрий')
        self.name.setStyleSheet("QLabel { color : white; }")
        self.name.setFont(QtGui.QFont('Arial', 25))
        self.nameLayout.addWidget(self.name)
        self.studyInfoLayout.addLayout(self.nameLayout)
        self.name.setHidden(True)

        self.patronymicLayout = QtWidgets.QVBoxLayout()
        self.patronymic = QtWidgets.QLabel('Александрович')
        self.patronymic.setStyleSheet("QLabel { color : white; }")
        self.patronymic.setFont(QtGui.QFont('Arial', 25))
        self.patronymicLayout.addWidget(self.patronymic)
        self.studyInfoLayout.addLayout(self.patronymicLayout)
        self.patronymic.setHidden(True)

        # Group
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

        # Degree
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

        # FormOfEducation
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

        # SpecialityCode
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

        # SpecialityName
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
        self.studyInfoLayout.addLayout(self.specialityNameLayout)
        self.staticSpecialityNameLabel.setHidden(True)
        self.specialityName.setHidden(True)

        # Content
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setStyleSheet("color: #00B6FF; font-size:14pt; background: #555555;")
        self.tabLessons = QtWidgets.QWidget()
        self.tabExams = QtWidgets.QWidget()
        self.tabGrades = QtWidgets.QWidget()
        self.tabEvents = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tabLessons, 'Расписание занятий')
        self.tabWidget.addTab(self.tabExams, 'Расписание сессии')
        self.tabWidget.addTab(self.tabGrades, 'Оценки')
        self.tabWidget.addTab(self.tabEvents, 'Мероприятия')
        self.tabWidget.setEnabled(False)
        self.contentLayout.addWidget(self.tabWidget)

        self.mainLayout.addLayout(self.menuLayout)
        self.mainLayout.addLayout(self.contentLayout)
        self.mainWidget.setLayout(self.withTitleLayout)
        self.menuLayout.setContentsMargins(20, 20, 20, 50)
        self.contentLayout.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(self.mainWidget)

    def func(self):
        return self.loginButton
