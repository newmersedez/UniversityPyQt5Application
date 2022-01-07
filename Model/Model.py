from .Student import *
from .Lesson import *
from .Exam import *
from .Grade import *
from .Event import *


class Model:
    def __init__(self):
        self._student = None
        self._lessons = None
        self._exams = None
        self._grades = None
        self._events = None

    def initStudent(self, student):
        self._student = student

    def initLessons(self, lessons):
        self._lessons = lessons

    def initExams(self, exams):
        self._exams = exams

    def initGrades(self, grades):
        self._grades = grades

    def initEvents(self, events):
        self._events = events

    def getStudent(self):
        return self._student

    def getLessons(self):
        return self._lessons

    def getExams(self):
        return self._exams

    def getGrades(self):
        return self._grades

    def getEvents(self):
        return self._events

    def removeStudent(self):
        self._student = None

    def removeLessons(self):
        self._lessons = None

    def removeExams(self):
        self._exams = None

    def removeGrades(self):
        self._grades = None

    def removeEvents(self):
        self._events = None

    def removeAll(self):
        self.removeStudent()
        self.removeLessons()
        self.removeExams()
        self.removeGrades()
        self.removeEvents()
