import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from process_text import process_text
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window's properties
        self.setWindowTitle("Text Processor")
        self.setGeometry(100, 100, 400, 200)  # x, y, width, height

        # Set up the layout
        layout = QVBoxLayout()

        # Create widgets
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Enter your text here...")
        self.process_button = QPushButton("Process Text")
        self.result_label = QLabel("Result will appear here...")

        # Add widgets to the layout
        layout.addWidget(self.input_text)
        layout.addWidget(self.process_button)
        layout.addWidget(self.result_label)

        # Set the central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect the button's click signal to the function that processes the text
        self.process_button.clicked.connect(self.on_process_button_clicked)

    def on_process_button_clicked(self):
        # Get the text from the input field
        input_text = self.input_text.text()
        # Process the text using the function defined earlier
        result_text = process_text(input_text)
        # Display the result in the label
        self.result_label.setText(result_text)

# Create and run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())