import sys
from View.View import *
from Model.Model import *
from Controller.Controller import *


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    model = Model()
    controller = Controller(model)
    view = View(model, controller)
    sys.exit(app.exec_())
