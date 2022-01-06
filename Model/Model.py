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

    def getStudent(self):
        return self._student

    def initLessons(self, lessons):
        self._lessons = lessons

    def getLessons(self):
        return self._lessons

    def initExams(self, exams):
        self._exams = exams

    def getExams(self):
        return self._exams

    def initGrades(self, grades):
        self._grades = grades

    def getGrades(self):
        return self._grades

    def initEvents(self, events):
        self._events = events

    def getEvents(self):
        return self._events
