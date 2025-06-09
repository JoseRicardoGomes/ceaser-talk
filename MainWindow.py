import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QLineEdit,
    QWidget,
    QFileDialog,
)
from PyQt6.QtGui import (
    QAction
)
from encrypton.ceaser import encode, decode

class MainWindow(QMainWindow):
    """
    MainWindow class implements a GUI for encoding and decoding text using the Caesar Cipher.
    
    Features:
    - Text input area for raw text
    - Text output area for encoded/decoded text (read-only)
    - Buttons to load text from a file, encode, decode, and clear output
    - Input field to specify the shift value for the cipher
    """
    
    def __init__(self):
        """
        Initialize the main window, set up the UI components and connect signals to their handlers.
        """
        super().__init__()
        self.setWindowTitle("Caesar Cipher Encoder")
        self.setup_ui()
        self.connect_signals()
        self.setup_menu()

    def setup_menu(self):
        """
        Sets up the menu bar and adds an 'Output' menu with a 'Clear Output' action.
        The Clear Output action clears the output text box when triggered.
        """
        menuBar = self.menuBar()

        outputMenu = menuBar.addMenu("Text")

        clearOutputAction = QAction("Clear Output", self)
        clearOutputAction.setShortcut("Ctrl+L")
        clearOutputAction.triggered.connect(self.clear_output)

        clearInputAction = QAction("Clear Input", self)
        clearInputAction.setShortcut("Ctrl+I")
        clearInputAction.triggered.connect(self.clear_input)

        outputMenu.addAction(clearInputAction)
        outputMenu.addAction(clearOutputAction)

    def setup_ui(self):
        """
        Set up the user interface components, including text edits, buttons, layouts, and container widget.
        """
        self.inputText = QTextEdit()
        self.outputText = QTextEdit()
        self.outputText.setReadOnly(True)

        self.loadButton = QPushButton("Load Text File")
        self.encodeButton = QPushButton("Encode")
        self.decodeButton = QPushButton("Decode")
        self.shiftInput = QLineEdit("4")
        self.shiftInput.setFixedWidth(40)

        # Layout for control buttons and shift input
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.loadButton)
        buttonLayout.addWidget(self.encodeButton)
        buttonLayout.addWidget(self.decodeButton)
        buttonLayout.addWidget(self.shiftInput)
        
        # Main vertical layout: input, buttons, output
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.inputText)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(self.outputText)

        # Set central widget with main layout
        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def connect_signals(self):
        """
        Connect UI signals (button clicks) to their corresponding slot methods.
        """
        self.loadButton.clicked.connect(self.load_text_file)
        self.encodeButton.clicked.connect(self.encode_text)
        self.decodeButton.clicked.connect(self.decode_text)

    def load_text_file(self):
        """
        Open a file dialog for the user to select a text file,
        then load its contents into the input text area.
        """
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Text File",
            "",
            "Text Files (*.txt);;All Files (*)"
        )
        if path:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.inputText.setPlainText(content)

    def get_shift_value(self):
        """
        Retrieve the integer shift value from the shift input field.
        Returns a default of 4 if the input is invalid.

        Returns:
            int: The shift value for the Caesar cipher.
        """
        try:
            return int(self.shiftInput.text())
        except ValueError:
            return 4  # Default fallback if invalid input

    def encode_text(self):
        """
        Encode the text from the input text area using the Caesar cipher
        and display the result in the output text area.
        """
        shift = self.get_shift_value()
        raw = self.inputText.toPlainText()
        encoded = encode(raw, shift)
        self.outputText.setPlainText(encoded)

    def decode_text(self):
        """
        Decode the text from the input text area using the Caesar cipher
        and display the result in the output text area.
        """
        shift = self.get_shift_value()
        raw = self.inputText.toPlainText()
        decoded = decode(raw, shift)
        self.outputText.setPlainText(decoded)

    def clear_output(self):
        """
        Clear the contents of the output text area.
        """
        self.outputText.setPlainText("")
    
    def clear_input(self):
        """
        Clear the contents of the input text area.
        """
        self.inputText.setPlainText("")