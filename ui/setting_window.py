
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class SettingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setting")
        self.setGeometry(300, 300, 400, 300)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("设置界面"))
        self.setLayout(layout)
