import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtGui import QColor, QPixmap, QFont
from PyQt5.QtCore import Qt

class QRCodeScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Code Scanner")

        # Get the screen geometry
        screen_geometry = QDesktopWidget().screenGeometry()

        # Calculate the desired width and height as a proportion of the screen size
        width = int(screen_geometry.width() * 0.8)  # 80% of screen width
        height = int(screen_geometry.height() * 0.6)  # 60% of screen height
        self.setGeometry(100, 100, width, height)

        layout = QVBoxLayout(self)

        # Outer container for the message
        outer_container = QWidget()
        outer_container.setAutoFillBackground(True)  # Allow background color to be set
        outer_palette = outer_container.palette()
        outer_palette.setColor(outer_container.backgroundRole(), QColor("#D3D3D3"))  # Slightly darker gray background color
        outer_container.setPalette(outer_palette)

        outer_container_layout = QVBoxLayout(outer_container)

        # Inner container for the message text with padding and rounded corners
        inner_container = QWidget()
        inner_container.setAutoFillBackground(True)  # Allow background color to be set
        inner_palette = inner_container.palette()
        inner_palette.setColor(inner_container.backgroundRole(), QColor("#ffffff"))  # White background color
        inner_container.setPalette(inner_palette)

        # Add padding and set rounded corners for the inner container
        inner_container.setStyleSheet("background-color: #ffffff; border-radius: 10px;")  # Set background color and border-radius
        
        inner_container_layout = QVBoxLayout(inner_container)  # Using QVBoxLayout instead of QHBoxLayout

        # Set fixed size or adjust size policy
        inner_container.setFixedWidth(int(width / 1.1))  # Adjust the width as needed
        inner_container.setFixedHeight(int(height * 1.2))  # Adjust the height as needed

        # Message
        message_label = QLabel(inner_container)
        message_label.setText("Please scan your QR code")
        message_label.setStyleSheet("font-size: 48px; color: #333; font-family: Arial, sans-serif;")  # Set font-family to sans-serif
        message_label.setAlignment(Qt.AlignCenter)  # Align the message label to the center

        # Image
        image_label = QLabel(inner_container)
        pixmap = QPixmap("images/pmelogo.png")  # Replace "images/pmelogo.png" with the path to your image
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)  # Align the image to the center

        # Add widgets to inner container layout
        inner_container_layout.addWidget(message_label, alignment=Qt.AlignCenter)  # Add message label to the layout
        inner_container_layout.addWidget(image_label, alignment=Qt.AlignCenter)  # Add image to the layout

        # Add inner container to outer container
        outer_container_layout.addWidget(inner_container, alignment=Qt.AlignCenter)  # Align the inner container to the center

        layout.addWidget(outer_container)

    def keyPressEvent(self, event):
        # Override keyPressEvent to print out any key pressed
        print(f"Key pressed: {event.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeScanner()
    window.show()
    sys.exit(app.exec_())
