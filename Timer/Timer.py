import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QWidget,
    QHBoxLayout, QVBoxLayout, QComboBox, QMessageBox
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QPainter, QColor, QPen
import qdarktheme


class CircularTimerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.time_text = "00:00:00"
        self.setMinimumSize(220, 220)
        self.font = QFont("Helvetica", 32, QFont.Bold)

    def setTimeText(self, text):
        self.time_text = text
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        # Draw the circle with some padding
        circle_rect = rect.adjusted(10, 10, -10, -10)

        # Background circle color
        painter.setBrush(QColor(50, 50, 50))  # dark gray
        # Border color and thickness
        painter.setPen(QPen(QColor(100, 100, 100), 6))
        painter.drawEllipse(circle_rect)

        # Draw the timer text centered inside the circle
        painter.setFont(self.font)
        painter.setPen(QColor(220, 220, 220))  # light gray text
        painter.drawText(rect, Qt.AlignCenter, self.time_text)


class CountdownApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Circular Stopwatch Timer with Unit Selector")
        self.setGeometry(100, 100, 360, 420)

        self.time_left = 0  # in seconds
        self.running = False

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        v_layout = QVBoxLayout()
        central_widget.setLayout(v_layout)

        # Circular timer widget
        self.circular_timer = CircularTimerWidget()
        v_layout.addWidget(self.circular_timer)

        # Input layout for number and units
        input_layout = QHBoxLayout()
        v_layout.addLayout(input_layout)

        # Entry for number input
        self.entry = QLineEdit()
        self.entry.setFont(QFont("Helvetica", 20))
        self.entry.setAlignment(Qt.AlignCenter)
        self.entry.setPlaceholderText("Enter number")
        self.entry.setText("1")  # default value
        input_layout.addWidget(self.entry)

        # Unit selector combo box
        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["seconds", "minutes", "hours"])
        self.unit_combo.setCurrentIndex(1)  # default "minutes"
        input_layout.addWidget(self.unit_combo)

        # Buttons layout
        h_layout = QHBoxLayout()
        v_layout.addLayout(h_layout)

        self.start_button = QPushButton("Start")
        self.start_button.setFixedWidth(90)
        self.start_button.clicked.connect(self.start_countdown)
        h_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.setFixedWidth(90)
        self.stop_button.clicked.connect(self.stop_countdown)
        self.stop_button.setEnabled(False)
        h_layout.addWidget(self.stop_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.setFixedWidth(90)
        self.reset_button.clicked.connect(self.reset_countdown)
        self.reset_button.setEnabled(False)
        h_layout.addWidget(self.reset_button)

        # QTimer to tick every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.countdown)

        # Initial label update
        self.update_label()

    def seconds_to_hms(self, seconds: int) -> str:
        """Convert seconds to HH:MM:SS format string."""
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        if h > 0:
            return f"{h:02}:{m:02}:{s:02}"
        else:
            return f"{m:02}:{s:02}"

    def update_label(self):
        time_str = self.seconds_to_hms(self.time_left)
        self.circular_timer.setTimeText(time_str)

    def countdown(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.update_label()
        else:
            self.timer.stop()
            self.running = False
            if self.time_left == 0:
                self.circular_timer.setTimeText("Time's up!")
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.reset_button.setEnabled(True)

    def start_countdown(self):
        if not self.running:
            try:
                value = int(self.entry.text())
                if value <= 0:
                    raise ValueError
            except ValueError:
                QMessageBox.warning(
                    self, "Invalid Input", "Please enter a positive integer for the time value."
                )
                return

            unit = self.unit_combo.currentText()
            if unit == "seconds":
                self.time_left = value
            elif unit == "minutes":
                self.time_left = value * 60
            elif unit == "hours":
                self.time_left = value * 3600
            else:
                self.time_left = value

            self.running = True
            self.update_label()
            self.timer.start(1000)
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.reset_button.setEnabled(False)

    def stop_countdown(self):
        if self.running:
            self.timer.stop()
            self.running = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.reset_button.setEnabled(True)

    def reset_countdown(self):
        self.timer.stop()
        self.running = False
        self.time_left = 0
        self.update_label()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.reset_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Enable HiDPI scaling (optional)
    qdarktheme.enable_hi_dpi()

    # Apply the dark theme
    qdarktheme.setup_theme()

    window = CountdownApp()
    window.show()

    sys.exit(app.exec())

