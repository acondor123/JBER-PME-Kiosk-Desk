import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class QRCodeScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Code Scanner")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Outer container for the message
        outer_container = QWidget()
        outer_container.setAutoFillBackground(True)  # Allow background color to be set
        outer_palette = outer_container.palette()
        outer_palette.setColor(outer_container.backgroundRole(), QColor("#dcdcdc"))  # Slightly darker gray background color
        outer_container.setPalette(outer_palette)

        outer_container_layout = QVBoxLayout()
        outer_container.setLayout(outer_container_layout)

        # Inner container for the message text with padding and smaller size
        inner_container = QWidget()
        inner_container.setAutoFillBackground(True)  # Allow background color to be set
        inner_palette = inner_container.palette()
        inner_palette.setColor(inner_container.backgroundRole(), QColor("#f0f0f0"))  # Light gray background color
        inner_container.setPalette(inner_palette)

        # Add padding and set a smaller size for the inner container
        inner_container.setStyleSheet("padding: 20px;")
        inner_container.setFixedWidth(700)
        inner_container.setFixedHeight(600)

        inner_container_layout = QHBoxLayout()  # Using QHBoxLayout to center the inner container
        inner_container.setLayout(inner_container_layout)

        # Message
        message_label = QLabel("Please scan your QR code")
        message_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")
        inner_container_layout.addWidget(message_label, alignment=Qt.AlignCenter)  # Align the message label to the center

        # Add inner container to outer container
        outer_container_layout.addWidget(inner_container, alignment=Qt.AlignCenter)  # Align the inner container to the center

        layout.addWidget(outer_container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeScanner()
    window.show()
    sys.exit(app.exec_())
