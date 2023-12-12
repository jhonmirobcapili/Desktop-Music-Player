import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from self import self

from main import MainWindow


class LoadingWindow(QWidget):
    def __init__(self):
        super(LoadingWindow, self).__init__()

        self.setGeometry(370, 160, 1200, 700)

        # Set the frameless window hint
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Insert the image in the frameless window
        self.background_label = QLabel(self)
        self.background_label.resize(1200, 700)
        self.background_label.setStyleSheet(
            "background-image: url(C:/Users/63939/PycharmProjects/Desktop Music Player/images/background.jpg);")
        self.background_label.show()

        # Create a timer
        self.timer = QTimer()

        # Show frameless window for 5 seconds and then quit the application. then open the main window of the application
        QTimer.singleShot(2000, self.open_main_window)

    def open_main_window(self):
        # Instantiate and show the main window
        self.main_window = MainWindow()
        self.main_window.show()

        # Close the frameless window
        self.close()


if __name__ == '__main__':
    # Create a QApplication instance
    app = QApplication(sys.argv)
    # Create an instance of the MainWindow class
    window = LoadingWindow()
    # Show the main window
    window.show()
    # Execute the application
    sys.exit(app.exec_())
