from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from Utils.ServerRequest import *
from Model.Model import *
import json


class Controller:
    def __init__(self, model):
        self._model = model
        self._view = None

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
                    QtWidgets.QMessageBox.about(self._view, "Ошибка", "Неправильный логин или пароль")
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
                QtWidgets.QMessageBox.about(self._view, "Ошибка", "Не удается установить соединение с сервером")

    def logoutButtonClick(self):
        self._toggleViewElementsVisibility(True)
        self._model.removeAll()

    def lessonsButtonClicked(self):
        print('lessons')

    def examsButtonClicked(self):
        print('exams')

    def gradesButtonClicked(self):
        print('grades')

    def eventsButtonClicked(self):
        print('events')
