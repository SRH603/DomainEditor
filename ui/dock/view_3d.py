
from PyQt5.QtWidgets import QDockWidget
from utils.gl_widget import GLWidget

class View3DDock(QDockWidget):
    def __init__(self, parent=None):
        super().__init__("3D视图", parent)
        self.setWidget(GLWidget())
        self.setFloating(False)
