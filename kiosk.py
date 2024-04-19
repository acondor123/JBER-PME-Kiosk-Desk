import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDesktopWidget
from PyQt5.QtGui import QColor, QMouseEvent, QPixmap, QFont, QMovie
from PyQt5.QtCore import Qt, QTimer
from Resources.validate import *

class QRCodeScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.scanned_code = ""
        self.currently_scanning = False
        self.data_fields = {
            "first_name": False,
            "last_name": False,
            "rank": False,
            "unit": False,
            "phone_number": False,
            "fitness": False,
            "profile": False
        }

        self.timer = QTimer()
        self.timer.timeout.connect(self.reset_scanned_code)

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

    def reset_data(self):
        self.data_fields = {
            "first_name": False,
            "last_name": False,
            "rank": False,
            "unit": False,
            "phone_number": False,
            "fitness": False,
            "profile": False
        }

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()

    def keyPressEvent(self, event):

        if event.text() != '$' and event.text() != "":
            self.scanned_code += event.text()
            if not self.currently_scanning:
                self.load_screen()
                self.currently_scanning = True
            self.timer.start(5000)
        elif self.scanned_code != "" and event.text() == "$":
            print(self.scanned_code)
            is_valid = self.validate_input(self.scanned_code)
            if(is_valid):
                self.update_spreadsheet()
                self.load_screen()
                self.show_checkmark_overlay()
            else:
                self.load_screen()
            self.scanned_code = ""
            self.currently_scanning = False
            time.sleep(0.5)
            self.timer.stop()

    def reset_scanned_code(self):
        self.scanned_code = ""
        self.load_screen()
        self.currently_scanning = False
        self.timer.stop()
        print("Timed out due to no terminal symbol.")

    def update_spreadsheet(self):
        '''
            todo: add logic to add entries to spreadsheet
            self.data_fields will have all entries stored in a dictionary for easy access
        '''
        print("ADD LOGIC FOR UPDATE_SPREADSHEET")

        #required in order to clear all fields previously in use
        self.reset_data()

    def validate_input(self, qr_data):
        valid_length = 7
        qr_data = qr_data.split(",")

        if(len(qr_data) > valid_length):
            print("Too much data")
            return False
        elif(len(qr_data) < valid_length):
            print("Not enough data")
            return False
        if(validateFirstName(qr_data[0])):
            self.data_fields["first_name"] = qr_data[0]
        if(validateLastName(qr_data[1])):
            self.data_fields["last_name"] = qr_data[1]
        if(validateRank(qr_data[2])):
            self.data_fields["rank"] = qr_data[2]
        if(validateUnit(qr_data[3])):
            self.data_fields["unit"] = qr_data[3]
        if(validatePhoneNumber(qr_data[4])):
            self.data_fields["phone_number"] = qr_data[4]
        if(validateFitness(qr_data[5])):
            self.data_fields["fitness"] = qr_data[5]
        if(validateProfile(qr_data[6])):
            self.data_fields["profile"] = qr_data[6]

        for key, value in self.data_fields.items():
            if(value is False):
                print(f"No value found for {key}")
                return False
            
        return True

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

    def show_checkmark_overlay(self):
        # Create a QLabel to display the GIF
        gif_label = QLabel(self)
        movie = QMovie("images/checkmark.gif")

        # Set the movie to play once and start it
        movie.loopCount = 1  # Set loop count to 1
        gif_label.setMovie(movie)
        movie.start()

        # Set the geometry of the QLabel to center it on the screen and scale it down
        screen_geometry = QApplication.desktop().screenGeometry()
        scale_factor = 0.5  # Adjust the scale factor as needed
        gif_width = int(movie.frameRect().width() * scale_factor)
        gif_height = int(movie.frameRect().height() * scale_factor)
        gif_label.setGeometry(
            (screen_geometry.width() - gif_width) // 2,
            (screen_geometry.height() - gif_height) // 2,
            gif_width,
            gif_height
        )

        # Set aspect ratio policy to keep the GIF aspect ratio when scaled
        gif_label.setScaledContents(True)

        # Connect a function to check if the movie has finished playing
        def check_movie_finished(frame_number):
            if frame_number == movie.frameCount() - 1:
                movie.stop()
                gif_label.close()

        # Connect the function to the frameChanged signal
        movie.frameChanged.connect(check_movie_finished)

        # Display the QLabel
        gif_label.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeScanner()
    window.show()
    sys.exit(app.exec_())