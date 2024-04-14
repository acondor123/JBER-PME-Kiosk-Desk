import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtGui import QColor, QPixmap, QFont
from PyQt5.QtCore import Qt

class QRCodeScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.scanned_code = ""

        self.setWindowTitle("QR Code Scanner")

        screen_geometry = QDesktopWidget().screenGeometry()

        width = int(screen_geometry.width() * 0.8)
        height = int(screen_geometry.height() * 0.6)
        self.setGeometry(100, 100, width, height)

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

    def keyPressEvent(self, event):
        if(event.key() == Qt.Key_Escape):
            self.showNormal()
        elif(event.key() == Qt.Key_F12):
            self.showFullScreen()
        elif(event.text() != '/'):
            self.scanned_code += event.text()
        else:
            print(self.scanned_code)
            self.scanned_code = ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeScanner()
    window.show()
    sys.exit(app.exec_())
