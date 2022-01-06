class Controller:
    def __init__(self, model):
        self._model = model
        self._view = None

    def setView(self, view):
        self._view = view

    def loginButtonClick(self):
        pass

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
