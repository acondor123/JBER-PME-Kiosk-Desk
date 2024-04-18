import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtGui import QColor, QPixmap, QFont, QMovie
from PyQt5.QtCore import Qt

class QRCodeScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.scanned_code = ""
        self.currently_scanning = False

        self.setWindowTitle("QR Code Scanner")

        screen_geometry = QDesktopWidget().screenGeometry()

        width = int(screen_geometry.width() * 0.8)
        height = int(screen_geometry.height() * 0.6)

        layout = QVBoxLayout(self)

        outer_container = QWidget()
        outer_container.setAutoFillBackground(True)
        outer_palette = outer_container.palette()
        outer_palette.setColor(outer_container.backgroundRole(), QColor("#D3D3D3"))
        outer_container.setPalette(outer_palette)

        outer_container_layout = QVBoxLayout(outer_container)

        inner_container = QWidget()
        inner_container.setAutoFillBackground(True)
        inner_palette = inner_container.palette()
        inner_palette.setColor(inner_container.backgroundRole(), QColor("#ffffff"))
        inner_container.setPalette(inner_palette)

        inner_container.setStyleSheet("background-color: #ffffff; border-radius: 10px;")

        inner_container_layout = QVBoxLayout(inner_container)

        inner_container.setFixedWidth(int(width / 1.1))
        inner_container.setFixedHeight(int(height * 1.2))

        message_label = QLabel(inner_container)
        message_label.setText("Please scan your QR code")
        message_label.setStyleSheet("font-size: 48px; color: #333; font-family: Arial, sans-serif;")
        message_label.setAlignment(Qt.AlignCenter)

        image_label = QLabel(inner_container)
        pixmap = QPixmap("images/pmelogo.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        inner_container_layout.addWidget(message_label, alignment=Qt.AlignCenter)
        inner_container_layout.addWidget(image_label, alignment=Qt.AlignCenter)

        outer_container_layout.addWidget(inner_container, alignment=Qt.AlignCenter)

        layout.addWidget(outer_container)

        self.loading_container = QWidget(self)
        self.loading_container.setGeometry(0, 0, screen_geometry.width(), screen_geometry.height())
        self.loading_container.setStyleSheet("background-color: rgba(255, 255, 255, 150);")
        self.loading_layout = QVBoxLayout(self.loading_container)
        self.loading_label = QLabel()
        self.loading_layout.addWidget(self.loading_label, alignment=Qt.AlignCenter)
        self.loading_container.hide()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:
            self.showNormal()
        elif event.key() == Qt.Key_F12:
            self.showFullScreen()
        elif event.text() != '$':
            self.scanned_code += event.text()
            if not self.currently_scanning:
                self.load_screen()
                self.currently_scanning = True
        else:
            print(self.scanned_code)
            self.validate_input()
            self.scanned_code = ""
            self.currently_scanning = False
            self.load_screen()

    def validate_input(self):
        pass

    def load_screen(self):
        if self.loading_container.isHidden():
            self.loading_movie = QMovie("images/loading.gif")
            self.loading_label.setMovie(self.loading_movie)
            self.loading_movie.start()
            self.loading_container.show()
            self.loading_container.raise_()
        else:
            self.loading_movie.stop()
            self.loading_container.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeScanner()
    window.show()
    sys.exit(app.exec_())