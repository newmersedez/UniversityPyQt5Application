from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR
from PyQt5 import QtWidgets, QtGui
from Utils.ServerRequest import *
from Model.Model import *
import json


class Controller:
    def __init__(self, model):
        self._model = model
        self._view = None

    def setView(self, view):
        self._view = view

    def loginButtonClick(self):
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

        ok = inputDialog.exec_()

        if ok:
            login = textBoxLogin.text()
            password = textBoxPassword.text()

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
                    self._model.initStudent(student)
                    obj = json.loads(recvText)

            except ConnectionError:
                QtWidgets.QMessageBox.about(self._view, "Ошибка", "Не удается установить соединение с сервером")

    def logoutButtonClick(self):
        pass

    def lessonsTabOpened(self):
        pass

    def examsTabOpened(self):
        pass

    def gradesTabOpened(self):
        pass

    def eventsTabOpened(self):
        pass
