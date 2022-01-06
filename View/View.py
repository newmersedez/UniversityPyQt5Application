from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._width = 1280
        self._height = 768

        self.resize(1280, 768)
        self.setFont(QtGui.QFont('Arial', 15))
        self.setStyleSheet("QWidget { background-color: #606060; }")

        self._configureLayouts()

    def _configureLayouts(self):
        # Main widget and layout
        self._mainWidget = QtWidgets.QWidget()
        self._withTitleLayout = QtWidgets.QVBoxLayout()
        self._mainLayout = QtWidgets.QHBoxLayout()

        # Menu and content layouts
        self._menuLayout = QtWidgets.QVBoxLayout()
        self._contentLayout = QtWidgets.QVBoxLayout()

        # Title
        self._titleLayout = QtWidgets.QHBoxLayout()
        self._title = QtWidgets.QLabel('Электронная зачетка МАИ')
        self._title.setFont(QtGui.QFont('Arial', 28))
        self._title.setStyleSheet("QLabel { color : white; }")
        self._titleLayout.addWidget(self._title)
        self._withTitleLayout.addLayout(self._titleLayout)
        self._withTitleLayout.addLayout(self._mainLayout)

        # Buttons
        self._loginLogoutLayout = QtWidgets.QVBoxLayout()
        self._loginButton = QtWidgets.QPushButton('Войти', self)
        self._loginButton.setStyleSheet("color: #00B6FF; font-size:14pt;")
        self._loginButton.setFixedSize(300, 40)
        self._logoutButton = QtWidgets.QPushButton('Выйти', self)
        self._logoutButton.setStyleSheet("color: #00B6FF; font-size:14pt;")
        self._logoutButton.setFixedSize(300, 40)
        self._logoutButton.setEnabled(False)
        self._loginLogoutLayout.addWidget(self._loginButton)
        self._loginLogoutLayout.addWidget(self._logoutButton)
        self._menuLayout.addLayout(self._loginLogoutLayout)

        # Menu layouts
        self._studyInfoLayout = QtWidgets.QVBoxLayout()
        self._menuLayout.addLayout(self._studyInfoLayout)

        # Lastname Name Patronymic
        self._lastnameLayout = QtWidgets.QVBoxLayout()
        self._lastname = QtWidgets.QLabel('Тришин')
        self._lastname.setStyleSheet("QLabel { color : white; }")
        self._lastname.setFont(QtGui.QFont('Arial', 25))
        self._lastnameLayout.addWidget(self._lastname)
        self._studyInfoLayout.addLayout(self._lastnameLayout)
        self._lastname.setHidden(True)

        self._nameLayout = QtWidgets.QVBoxLayout()
        self._name = QtWidgets.QLabel('Дмитрий')
        self._name.setStyleSheet("QLabel { color : white; }")
        self._name.setFont(QtGui.QFont('Arial', 25))
        self._nameLayout.addWidget(self._name)
        self._studyInfoLayout.addLayout(self._nameLayout)
        self._name.setHidden(True)

        self._patronymicLayout = QtWidgets.QVBoxLayout()
        self._patronymic = QtWidgets.QLabel('Александрович')
        self._patronymic.setStyleSheet("QLabel { color : white; }")
        self._patronymic.setFont(QtGui.QFont('Arial', 25))
        self._patronymicLayout.addWidget(self._patronymic)
        self._studyInfoLayout.addLayout(self._patronymicLayout)
        self._patronymic.setHidden(True)

        # Group
        self._groupLayout = QtWidgets.QVBoxLayout()
        self._staticGroupLabel = QtWidgets.QLabel('Группа')
        self._staticGroupLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self._staticGroupLabel.setFont(QtGui.QFont('Arial', 14))
        self._group = QtWidgets.QLabel('М8О-311Б-19')
        self._group.setStyleSheet("QLabel { color : white; }")
        self._group.setFont(QtGui.QFont('Arial', 18))
        self._groupLayout.addWidget(self._staticGroupLabel)
        self._groupLayout.addWidget(self._group)
        self._studyInfoLayout.addLayout(self._groupLayout)
        self._group.setHidden(True)
        self._staticGroupLabel.setHidden(True)

        # Degree
        self._degreeLayout = QtWidgets.QVBoxLayout()
        self._staticDegreeLabel = QtWidgets.QLabel('Образование')
        self._staticDegreeLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self._staticDegreeLabel.setFont(QtGui.QFont('Arial', 14))
        self._degree = QtWidgets.QLabel('Бакалавриат')
        self._degree.setStyleSheet("QLabel { color : white; }")
        self._degree.setFont(QtGui.QFont('Arial', 18))
        self._degreeLayout.addWidget(self._staticDegreeLabel)
        self._degreeLayout.addWidget(self._degree)
        self._studyInfoLayout.addLayout(self._degreeLayout)
        self._staticDegreeLabel.setHidden(True)
        self._degree.setHidden(True)

        # FormOfEducation
        self._formOfEducationLayout = QtWidgets.QVBoxLayout()
        self._staticFormOfEducationLabel = QtWidgets.QLabel('Форма обучения')
        self._staticFormOfEducationLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self._staticFormOfEducationLabel.setFont(QtGui.QFont('Arial', 14))
        self._formOfEducation = QtWidgets.QLabel('Очная')
        self._formOfEducation.setStyleSheet("QLabel { color : white; }")
        self._formOfEducation.setFont(QtGui.QFont('Arial', 18))
        self._formOfEducationLayout.addWidget(self._staticFormOfEducationLabel)
        self._formOfEducationLayout.addWidget(self._formOfEducation)
        self._studyInfoLayout.addLayout(self._formOfEducationLayout)
        self._staticFormOfEducationLabel.setHidden(True)
        self._formOfEducation.setHidden(True)

        # SpecialityCode
        self._specialityCodeLayout = QtWidgets.QVBoxLayout()
        self._staticCodeLabel = QtWidgets.QLabel('Код специальности')
        self._staticCodeLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self._staticCodeLabel.setFont(QtGui.QFont('Arial', 14))
        self._specialityCode = QtWidgets.QLabel('02.03.02')
        self._specialityCode.setStyleSheet("QLabel { color : white; }")
        self._specialityCode.setFont(QtGui.QFont('Arial', 18))
        self._specialityCodeLayout.addWidget(self._staticCodeLabel)
        self._specialityCodeLayout.addWidget(self._specialityCode)
        self._studyInfoLayout.addLayout(self._specialityCodeLayout)
        self._staticCodeLabel.setHidden(True)
        self._specialityCode.setHidden(True)

        # SpecialityName
        self._specialityNameLayout = QtWidgets.QVBoxLayout()
        self._staticSpecialityNameLabel = QtWidgets.QLabel('Направление')
        self._staticSpecialityNameLabel.setStyleSheet("QLabel { color : #00B6FF; }")
        self._staticSpecialityNameLabel.setFont(QtGui.QFont('Arial', 14))
        self._specialityName = QtWidgets.QLabel('Фундаментальная информатика и информационные технологии')
        self._specialityName.setWordWrap(True)
        self._specialityName.setFixedSize(300, 100)
        self._specialityName.setStyleSheet("QLabel { color : white; }")
        self._specialityName.setFont(QtGui.QFont('Arial', 18))
        self._specialityNameLayout.addWidget(self._staticSpecialityNameLabel)
        self._specialityNameLayout.addWidget(self._specialityName)
        self._studyInfoLayout.addLayout(self._specialityNameLayout)
        self._staticSpecialityNameLabel.setHidden(True)
        self._specialityName.setHidden(True)

        # Content
        self._tabWidget = QtWidgets.QTabWidget()
        self._tabWidget.setStyleSheet("color: #00B6FF; font-size:14pt; background: #555555;")
        self._tabLessons = QtWidgets.QWidget()
        self._tabExams = QtWidgets.QWidget()
        self._tabGrades = QtWidgets.QWidget()
        self._tabEvents = QtWidgets.QWidget()
        self._tabWidget.addTab(self._tabLessons, 'Расписание занятий')
        self._tabWidget.addTab(self._tabExams, 'Расписание сессии')
        self._tabWidget.addTab(self._tabGrades, 'Оценки')
        self._tabWidget.addTab(self._tabEvents, 'Мероприятия')
        self._tabWidget.setEnabled(False)
        self._contentLayout.addWidget(self._tabWidget)

        self._mainLayout.addLayout(self._menuLayout)
        self._mainLayout.addLayout(self._contentLayout)
        self._mainWidget.setLayout(self._withTitleLayout)
        self._menuLayout.setContentsMargins(20, 20, 20, 50)
        self._contentLayout.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(self._mainWidget)
