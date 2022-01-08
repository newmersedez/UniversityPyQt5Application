from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR
from PyQt5 import QtWidgets, QtGui, QtCore
from Utils.ServerRequest import *
from Model.Model import *
from View.View import *
import json


class Controller:
    def __init__(self, model):
        self._model = model
        self._view = None

    # Utils
    def setView(self, view):
        self._view = view

    def _execLoginDialog(self):
        inputDialog = QtWidgets.QDialog(self._view)
        inputDialog.setWindowTitle('Авторизация')
        inputDialog.setFixedSize(300, 200)
        form = QtWidgets.QFormLayout(inputDialog)

        labelLogin = QtWidgets.QLabel('Логин')
        labelLogin.setStyleSheet("QLabel { color : white; }")
        labelLogin.setFont(QtGui.QFont('Arial', 12))
        textBoxLogin = QtWidgets.QLineEdit()
        textBoxLogin.setFont(QtGui.QFont('Arial', 14))
        textBoxLogin.setStyleSheet("QLineEdit { color : #00B6FF; }")

        labelPassword = QtWidgets.QLabel('Пароль')
        labelPassword.setStyleSheet("QLabel { color : white; }")
        labelPassword.setFont(QtGui.QFont('Arial', 12))
        labelPassword.setContentsMargins(0, 20, 0, 0)
        textBoxPassword = QtWidgets.QLineEdit()
        textBoxPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        textBoxPassword.setFont(QtGui.QFont('Arial', 14))
        textBoxPassword.setStyleSheet("QLineEdit { color : #00B6FF; }")

        form.addRow(labelLogin)
        form.addRow(textBoxLogin)
        form.addRow(labelPassword)
        form.addRow(textBoxPassword)

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        buttonBox.setStyleSheet("QPushButton { color : white; }")
        form.addRow(buttonBox)
        buttonBox.accepted.connect(inputDialog.accept)
        buttonBox.rejected.connect(inputDialog.reject)

        status = inputDialog.exec_()
        login = textBoxLogin.text()
        password = textBoxPassword.text()
        return status, login, password

    def _execErrorMessageBox(self, message: str):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Ошибка")
        msg.setStyleSheet('background-color : #606060; color : white; font-size : 12pt')
        msg.exec_()

    # Default user
    def _toggleViewElementsVisibility(self, value: bool):
        self._view.loginButton.setEnabled(value)
        self._view.logoutButton.setEnabled(not value)
        self._view.lessonsButton.setHidden(value)
        self._view.examsButton.setHidden(value)
        self._view.gradesButton.setHidden(value)
        self._view.eventsButton.setHidden(value)
        self._view.table.setHidden(value)

        self._view.lastname.setHidden(value)
        self._view.name.setHidden(value)
        self._view.patronymic.setHidden(value)

        self._view.staticGroupLabel.setHidden(value)
        self._view.group.setHidden(value)

        self._view.staticDegreeLabel.setHidden(value)
        self._view.degree.setHidden(value)

        self._view.staticFormOfEducationLabel.setHidden(value)
        self._view.formOfEducation.setHidden(value)

        self._view.staticCodeLabel.setHidden(value)
        self._view.specialityCode.setHidden(value)

        self._view.staticSpecialityNameLabel.setHidden(value)
        self._view.specialityName.setHidden(value)

    def loginButtonClick(self):
        status, login, password = self._execLoginDialog()

        if status:
            # Create server request
            serverRequest = ServerRequest()
            serverRequest.RequestName = 'Auth'
            serverRequest.Args = [login, password]
            jsonText = json.dumps(serverRequest.__dict__)

            try:
                # Send request to server
                s = socket(AF_INET, SOCK_STREAM)
                s.connect(('localhost', 5430))
                s.send(str.encode(jsonText))

                # Get request from server
                bytes_buffer = s.recv(1024)
                recvText = bytes_buffer.decode('utf-8')
                s.shutdown(SHUT_RDWR)
                s.close()
                if recvText == '[]':
                    self._execErrorMessageBox('Неправильный логин или пароль')
                else:
                    if login == 'admin' and password == 'admin':
                        self._adminToggleViewElementsVisibility(True)
                    else:
                        student = Student()
                        obj = json.loads(recvText)
                        student.StudentLastname = obj[0]['StudentLastname']
                        student.StudentName = obj[0]['StudentName']
                        student.StudentPatronymic = obj[0]['StudentPatronymic']
                        student.StudentGroup = obj[0]['StudentGroup']
                        student.StudentDegree = obj[0]['StudentDegree']
                        student.StudentFormOfEducation = obj[0]['StudentFormOfEducation']
                        student.SpecialtyNumber = obj[0]['SpecialtyNumber']
                        student.SpecialtyName = obj[0]['SpecialtyName']
                        self._toggleViewElementsVisibility(False)
                        self._model.initStudent(student)
                        self._view.lastname.setText(student.StudentLastname)
                        self._view.name.setText(student.StudentName)
                        self._view.patronymic.setText(student.StudentPatronymic)
                        self._view.group.setText(student.StudentGroup)
                        self._view.degree.setText(student.StudentDegree)
                        self._view.formOfEducation.setText(student.StudentFormOfEducation)
                        self._view.specialityCode.setText(student.SpecialtyNumber)
                        self._view.specialityName.setText(student.SpecialtyName)
            except ConnectionError:
                self._execErrorMessageBox('Не удалось установить соединение с сервером')

    def logoutButtonClick(self):
        self._view.table.setRowCount(0)
        self._view.table.setColumnCount(0)
        self._adminToggleViewElementsVisibility(False)
        self._toggleViewElementsVisibility(True)
        self._model.removeAll()

    def lessonsButtonClicked(self):
        serverRequest = ServerRequest()
        serverRequest.RequestName = 'Lessons'
        serverRequest.Args.append(self._model.getStudent().StudentGroup)
        jsonText = json.dumps(serverRequest.__dict__)

        try:
            # Send request to server
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', 5430))
            s.send(str.encode(jsonText))

            # Get request from server
            bytes_buffer = s.recv(10000)
            recvText = bytes_buffer.decode('utf-8')
            s.shutdown(SHUT_RDWR)
            s.close()
            obj = json.loads(recvText)

            if len(obj) > 0:
                self._view.table.setColumnCount(len(obj[0]))
                self._view.table.setRowCount(len(obj))
                self._view.table.setHorizontalHeaderLabels(
                    ['День недели', 'Время', 'Тип занятий', 'Аудитория', 'Предмет'])
                for i in range(len(obj)):
                    self._view.table.setItem(i, 0, QtWidgets.QTableWidgetItem(obj[i]['LessonDay']))
                    self._view.table.setItem(i, 1, QtWidgets.QTableWidgetItem(obj[i]['LessonTime']))
                    self._view.table.setItem(i, 2, QtWidgets.QTableWidgetItem(obj[i]['LessonType']))
                    self._view.table.setItem(i, 3, QtWidgets.QTableWidgetItem(obj[i]['ClassroomName']))
                    self._view.table.setItem(i, 4, QtWidgets.QTableWidgetItem(obj[i]['SubjectName']))
                self._view.table.resizeColumnsToContents()

        except ConnectionError:
            self._execErrorMessageBox('Не удалось установить соединение с сервером')

    def examsButtonClicked(self):
        serverRequest = ServerRequest()
        serverRequest.RequestName = 'Exams'
        serverRequest.Args.append(self._model.getStudent().StudentGroup)
        jsonText = json.dumps(serverRequest.__dict__)

        try:
            # Send request to server
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', 5430))
            s.send(str.encode(jsonText))

            # Get request from server
            bytes_buffer = s.recv(10000)
            recvText = bytes_buffer.decode('utf-8')
            s.shutdown(SHUT_RDWR)
            s.close()
            obj = json.loads(recvText)

            if len(obj) > 0:
                self._view.table.setColumnCount(len(obj[0]))
                self._view.table.setRowCount(len(obj))
                self._view.table.setHorizontalHeaderLabels(
                    ['Предмет', 'Группа', 'Дата', 'Время', 'Аудитория'])
                for i in range(len(obj)):
                    self._view.table.setItem(i, 0, QtWidgets.QTableWidgetItem(obj[i]['SubjectName']))
                    self._view.table.setItem(i, 1, QtWidgets.QTableWidgetItem(obj[i]['GroupName']))
                    self._view.table.setItem(i, 2, QtWidgets.QTableWidgetItem(obj[i]['ExamDate']))
                    self._view.table.setItem(i, 3, QtWidgets.QTableWidgetItem(obj[i]['ExamTime']))
                    self._view.table.setItem(i, 4, QtWidgets.QTableWidgetItem(obj[i]['ClassroomName']))
                self._view.table.resizeColumnsToContents()

        except ConnectionError:
            self._execErrorMessageBox('Не удалось установить соединение с сервером')

    def gradesButtonClicked(self):
        serverRequest = ServerRequest()
        serverRequest.RequestName = 'Marks'
        serverRequest.Args.append(self._model.getStudent().StudentLastname)
        serverRequest.Args.append(self._model.getStudent().StudentName)
        serverRequest.Args.append(self._model.getStudent().StudentPatronymic)
        jsonText = json.dumps(serverRequest.__dict__)

        try:
            # Send request to server
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', 5430))
            s.send(str.encode(jsonText))

            # Get request from server
            bytes_buffer = s.recv(10000)
            recvText = bytes_buffer.decode('utf-8')
            s.shutdown(SHUT_RDWR)
            s.close()
            obj = json.loads(recvText)

            if len(obj) > 0:
                self._view.table.setColumnCount(len(obj[0]))
                self._view.table.setRowCount(len(obj))
                self._view.table.setHorizontalHeaderLabels(
                    ['Фамилия', 'Имя', 'Отчество', 'Предмет', 'Оценка'])
                for i in range(len(obj)):
                    self._view.table.setItem(i, 0, QtWidgets.QTableWidgetItem(obj[i]['StudentLastname']))
                    self._view.table.setItem(i, 1, QtWidgets.QTableWidgetItem(obj[i]['StudentName']))
                    self._view.table.setItem(i, 2, QtWidgets.QTableWidgetItem(obj[i]['StudentPatronymic']))
                    self._view.table.setItem(i, 3, QtWidgets.QTableWidgetItem(obj[i]['SubjectName']))
                    self._view.table.setItem(i, 4, QtWidgets.QTableWidgetItem(obj[i]['Grade']))
                self._view.table.resizeColumnsToContents()

        except ConnectionError:
            self._execErrorMessageBox('Не удалось установить соединение с сервером')

    def eventsButtonClicked(self):
        serverRequest = ServerRequest()
        serverRequest.RequestName = 'Events'
        jsonText = json.dumps(serverRequest.__dict__)

        try:
            # Send request to server
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', 5430))
            s.send(str.encode(jsonText))

            # Get request from server
            bytes_buffer = s.recv(10000)
            recvText = bytes_buffer.decode('utf-8')
            s.shutdown(SHUT_RDWR)
            s.close()
            obj = json.loads(recvText)

            if len(obj) > 0:
                self._view.table.setColumnCount(len(obj[0]))
                self._view.table.setRowCount(len(obj))
                self._view.table.setHorizontalHeaderLabels(
                    ['Названеие', 'Дата', 'Время', 'Аудитория', 'Группа'])
                for i in range(len(obj)):
                    self._view.table.setItem(i, 0, QtWidgets.QTableWidgetItem(obj[i]['EventName']))
                    self._view.table.setItem(i, 1, QtWidgets.QTableWidgetItem(obj[i]['EventDate']))
                    self._view.table.setItem(i, 2, QtWidgets.QTableWidgetItem(obj[i]['EventTime']))
                    self._view.table.setItem(i, 3, QtWidgets.QTableWidgetItem(obj[i]['ClassroomName']))
                    self._view.table.setItem(i, 4, QtWidgets.QTableWidgetItem(obj[i]['GroupName']))
                self._view.table.resizeColumnsToContents()

        except ConnectionError:
            self._execErrorMessageBox('Не удалось установить соединение с сервером')

    # Admin user
    def _adminToggleViewElementsVisibility(self, value: bool):
        self._view.lastname.setHidden(value)
        self._view.name.setText('Superuser: admin')
        self._view.name.setHidden(not value)
        self._view.patronymic.setHidden(value)
        self._view.staticGroupLabel.setHidden(value)
        self._view.group.setHidden(value)
        self._view.staticDegreeLabel.setHidden(value)
        self._view.degree.setHidden(value)
        self._view.staticFormOfEducationLabel.setHidden(value)
        self._view.formOfEducation.setHidden(value)
        self._view.staticCodeLabel.setHidden(value)
        self._view.specialityCode.setHidden(value)
        self._view.staticSpecialityNameLabel.setHidden(value)
        self._view.specialityName.setHidden(value)
        self._view.adminChangeLoginButton.setHidden(not value)
        self._view.adminChangePasswordButton.setHidden(not value)
        self._view.table.setHidden(not value)
        self._view.adminStudentsButton.setHidden(not value)
        self._view.adminLecturersButton.setHidden(not value)
        self._view.loginButton.setEnabled(not value)
        self._view.logoutButton.setEnabled(value)

    def adminStudentsButtonClick(self):
        serverRequest = ServerRequest()
        serverRequest.RequestName = 'AdminStudents'
        jsonText = json.dumps(serverRequest.__dict__)

        try:
            # Send request to server
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', 5430))
            s.send(str.encode(jsonText))

            # Get request from server
            bytes_buffer = s.recv(10000)
            recvText = bytes_buffer.decode('utf-8')
            s.shutdown(SHUT_RDWR)
            s.close()
            obj = json.loads(recvText)

            if len(obj) > 0:
                self._view.table.setColumnCount(len(obj[0]))
                self._view.table.setRowCount(len(obj))
                self._view.table.setHorizontalHeaderLabels(
                    ['ID', 'Фамилия', 'Имя', 'Отчество', 'Логин', 'Пароль'])
                for i in range(len(obj)):
                    self._view.table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(obj[i]['StudentID'])))
                    self._view.table.setItem(i, 1, QtWidgets.QTableWidgetItem(obj[i]['StudentLastname']))
                    self._view.table.setItem(i, 2, QtWidgets.QTableWidgetItem(obj[i]['StudentName']))
                    self._view.table.setItem(i, 3, QtWidgets.QTableWidgetItem(obj[i]['StudentPatronymic']))
                    self._view.table.setItem(i, 4, QtWidgets.QTableWidgetItem(obj[i]['StudentLogin']))
                    self._view.table.setItem(i, 5, QtWidgets.QTableWidgetItem(obj[i]['StudentPassword']))
                self._view.table.resizeColumnsToContents()

        except ConnectionError:
            self._execErrorMessageBox('Не удалось установить соединение с сервером')

    def adminLecturersButtonClick(self):
        pass
        serverRequest = ServerRequest()
        serverRequest.RequestName = 'AdminLecturers'
        jsonText = json.dumps(serverRequest.__dict__)

        try:
            # Send request to server
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', 5430))
            s.send(str.encode(jsonText))

            # Get request from server
            bytes_buffer = s.recv(10000)
            recvText = bytes_buffer.decode('utf-8')
            s.shutdown(SHUT_RDWR)
            s.close()
            obj = json.loads(recvText)

            if len(obj) > 0:
                self._view.table.setColumnCount(len(obj[0]))
                self._view.table.setRowCount(len(obj))
                self._view.table.setHorizontalHeaderLabels(
                    ['ID', 'Фамилия', 'Имя', 'Отчество', 'Предмет'])
                for i in range(len(obj)):
                    self._view.table.setItem(i, 0, QtWidgets.QTableWidgetItem(obj[i]['LecturerID']))
                    self._view.table.setItem(i, 1, QtWidgets.QTableWidgetItem(obj[i]['LecturerLastname']))
                    self._view.table.setItem(i, 2, QtWidgets.QTableWidgetItem(obj[i]['LecturerName']))
                    self._view.table.setItem(i, 3, QtWidgets.QTableWidgetItem(obj[i]['LecturerPatronymic']))
                    self._view.table.setItem(i, 4, QtWidgets.QTableWidgetItem(obj[i]['SubjectName']))
                self._view.table.resizeColumnsToContents()

        except ConnectionError:
            self._execErrorMessageBox('Не удалось установить соединение с сервером')

    def adminStudentChangeLogin(self):
        inputDialog = QtWidgets.QDialog(self._view)
        inputDialog.setStyleSheet('background-color : #606060; color : white; font-size : 12pt')
        inputDialog.setWindowTitle('Замена логина пользователя')
        inputDialog.setFont(QtGui.QFont('Arial', 15))
        form = QtWidgets.QFormLayout(inputDialog)

        textBox1 = QtWidgets.QSpinBox()
        textBox1.setMinimum(1)
        textBox1.setMaximum(1000000)
        form.addRow(QtWidgets.QLabel('ID студента'))
        form.addRow(textBox1)

        textBox2 = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel('Новый логин'))
        form.addRow(textBox2)

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
        form.addRow(buttonBox)
        buttonBox.accepted.connect(inputDialog.accept)

        ok = inputDialog.exec_()

        if ok:
            student_id = int(textBox1.text())
            new_login = textBox2.text()
            print(student_id, new_login)

            if len(new_login) == 0:
                self._execErrorMessageBox('Новый логин не может быть пустым')
            else:
                serverRequest = ServerRequest()
                serverRequest.RequestName = 'AdminChangeLogin'
                serverRequest.Args.append(student_id)
                serverRequest.Args.append(new_login)
                jsonText = json.dumps(serverRequest.__dict__)
                try:
                    s = socket(AF_INET, SOCK_STREAM)
                    s.connect(('localhost', 5430))
                    s.send(str.encode(jsonText))
                    s.shutdown(SHUT_RDWR)
                    s.close()

                except ConnectionError:
                    self._execErrorMessageBox('Не удалось установить соединение с сервером')

    def adminStudentChangePassword(self):
        inputDialog = QtWidgets.QDialog(self._view)
        inputDialog.setStyleSheet('background-color : #606060; color : white; font-size : 12pt')
        inputDialog.setWindowTitle('Замена пароль пользователя')
        inputDialog.setFont(QtGui.QFont('Arial', 15))
        form = QtWidgets.QFormLayout(inputDialog)

        textBox1 = QtWidgets.QSpinBox()
        textBox1.setMinimum(1)
        textBox1.setMaximum(1000000)
        form.addRow(QtWidgets.QLabel('ID студента'))
        form.addRow(textBox1)

        textBox2 = QtWidgets.QLineEdit()
        form.addRow(QtWidgets.QLabel('Новый пароль'))
        form.addRow(textBox2)

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
        form.addRow(buttonBox)
        buttonBox.accepted.connect(inputDialog.accept)

        ok = inputDialog.exec_()

        if ok:
            student_id = int(textBox1.text())
            new_passwd = textBox2.text()
            print(student_id, new_passwd)

            if len(new_passwd) == 0:
                self._execErrorMessageBox('Новый логин не может быть пустым')
            else:
                serverRequest = ServerRequest()
                serverRequest.RequestName = 'AdminChangePassword'
                serverRequest.Args.append(student_id)
                serverRequest.Args.append(new_passwd)
                jsonText = json.dumps(serverRequest.__dict__)
                try:
                    s = socket(AF_INET, SOCK_STREAM)
                    s.connect(('localhost', 5430))
                    s.send(str.encode(jsonText))
                    s.shutdown(SHUT_RDWR)
                    s.close()

                except ConnectionError:
                    self._execErrorMessageBox('Не удалось установить соединение с сервером')
