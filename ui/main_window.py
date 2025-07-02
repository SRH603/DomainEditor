
from PyQt5.QtWidgets import QMainWindow, QAction, QDockWidget, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ui.setting_window import SettingWindow
from ui.dock.view_3d import View3DDock

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setting_window = None
        self.setWindowTitle("SpectrumEditor")
        self.setGeometry(200, 200, 1000, 700)
        self.init_ui()

    def init_ui(self):
        self.statusBar().showMessage("Ready")

        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction("New", lambda: self.statusBar().showMessage("New File"))
        file_menu.addAction("Open", lambda: self.statusBar().showMessage("Open File"))
        file_menu.addAction("Exit", self.close)

        # Edit Menu
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # View Menu
        view_menu = menubar.addMenu("View")

        # Tool Menu
        tool_menu = menubar.addMenu("Tool")
        tool_menu.addAction("Run Tool", lambda: QMessageBox.information(self, "Tool", "Tool is running..."))

        # Window Menu
        window_menu = menubar.addMenu("Window")
        window_menu.addAction("3D视图", self.open_3d_view)

        # Help Menu
        help_menu = menubar.addMenu("Help")
        help_menu.addAction("About", lambda: QMessageBox.about(self, "About", "SpectrumEditor using PyQt5"))

        # macOS App menu (extra Setting)
        self.add_app_menu()

    def add_app_menu(self):
        setting_action = QAction("Setting", self)
        setting_action.triggered.connect(self.open_setting)
        self.menuBar().addMenu("SpectrumEditor").addAction(setting_action)

    def open_setting(self):
        if not self.setting_window:
            self.setting_window = SettingWindow()
        self.setting_window.show()
        self.setting_window.raise_()
        self.setting_window.activateWindow()

    def open_3d_view(self):
        self.view3d = View3DDock(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.view3d)
