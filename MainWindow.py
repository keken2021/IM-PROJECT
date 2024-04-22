import sys
import add_design
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from Icons import icons

class login(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('loginpage.ui', self)
        self.loginbutton.clicked.connect(self.open_dashboard)

    def open_dashboard(self):
        self.dashboard = dashboard()
        self.dashboard.show()
        self.close()

class dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('menu.ui', self)

        self.dashboard_2.clicked.connect(self.switch_to_dashboard)
        self.designs_2.clicked.connect(self.switch_to_design)
        self.employees_2.clicked.connect(self.switch_to_employee)
        self.mediafiles.clicked.connect(self.switch_to_mediafiles)
        self.sales_2.clicked.connect(self.switch_to_sales)    


    def switch_to_dashboard(self):
                self.stackedWidget.setCurrentIndex(0)

    def switch_to_design(self):
                self.stackedWidget.setCurrentIndex(1)
                

    def switch_to_employee(self):
                self.stackedWidget.setCurrentIndex(2)

    def switch_to_mediafiles(self):
                self.stackedWidget.setCurrentIndex(3)

    def switch_to_sales(self):
                self.stackedWidget.setCurrentIndex(4)

class add_design(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('add_design.ui', self)
        self.searchbutton_3.clicked.connect(self.open_adddesign_window)

    def open_adddesign_window(self):
        self.close()  # Close the current window
        self.adddesign_window = AddDesign()  # Create a new AddDesign instance
        self.adddesign_window.show()

class AddDesign(QMainWindow):
    def __init__(self):
           super().__init__()
           loadUi('add_design.ui',self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = login()
    window1.setWindowTitle("DRILAB")
    window1.show()
    sys.exit(app.exec_())