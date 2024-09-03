import os
import sys
import subprocess
from abc import ABC, abstractmethod
from PIL import Image, ExifTags
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QComboBox

class ImageConverter(ABC):
    @abstractmethod
    def convert(self, input_path: str, output_path: str) -> bool:
        pass

class CR3Converter(ImageConverter):
    def convert(self, input_path: str, output_path: str) -> bool:
        command = ['exiftool', '-b', '-JpgFromRaw', input_path]
        try:
            with open(output_path, 'wb') as f:
                subprocess.run(command, check=True, stdout=f)
            return True
        except subprocess.CalledProcessError as e:
            print(f'Error: {e}')
            return False

class ImageFileConverter(ImageConverter):
    def convert(self, input_path: str, output_path: str) -> bool:
        try:
            image = ImageConverterHelper.check_image_orientation(Image.open(input_path))
            image.save(output_path)
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

class ImageConverterFactory:
    @staticmethod
    def get_converter(file_extension: str) -> ImageConverter:
        if file_extension.lower() == '.cr3':
            return CR3Converter()
        else:
            return ImageFileConverter()

class ImageConverterHelper:
    @staticmethod
    def check_image_orientation(image):
        try:
            exif = image._getexif()
            if exif is not None:
                orientation = next((tag for tag, value in ExifTags.TAGS.items() if value == 'Orientation'), None)

                if orientation and orientation in exif:
                    if exif[orientation] == 3:
                        image = image.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        image = image.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        image = image.rotate(90, expand=True)
            return image
        except (AttributeError, KeyError, IndexError) as e:
            print(f'Error: {e}')
            return image

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.type_list = ['jpg', 'png', 'jpeg', 'webp']
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.file_label = QLabel('Select a CR3 file or folder:', self)
        layout.addWidget(self.file_label)

        self.file_button = QPushButton('Browse Image File', self)
        self.file_button.clicked.connect(self.select_file)
        layout.addWidget(self.file_button)

        self.folder_button = QPushButton('Browse Images Folder', self)
        self.folder_button.clicked.connect(self.select_folder)
        layout.addWidget(self.folder_button)

        self.output_label = QLabel('Select an output folder:', self)
        layout.addWidget(self.output_label)

        self.output_button = QPushButton('Browse Output Folder', self)
        self.output_button.clicked.connect(self.select_output_folder)
        layout.addWidget(self.output_button)

        self.format_label = QLabel('Select output format:', self)
        layout.addWidget(self.format_label)

        self.format_combo = QComboBox(self)
        self.format_combo.addItems(self.type_list)
        layout.addWidget(self.format_combo)

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.clicked.connect(self.convert_file)
        layout.addWidget(self.convert_button)

        self.status_label = QLabel('', self)
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.setWindowTitle('Image Converter')
        self.setGeometry(300, 300, 400, 200)

    def select_file(self):
        options = QFileDialog.Options()
        self.image_file, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.cr3 *.jpg *.png *.jpeg);;All Files (*)", options=options)
        self.image_folder = None
        if self.image_file:
            self.file_label.setText(f'Selected file: {self.image_file}')

    def select_folder(self):
        self.image_folder = QFileDialog.getExistingDirectory(self, "Select Folder Containing Image Files")
        self.image_file = None
        if self.image_folder:
            self.file_label.setText(f'Selected folder: {self.image_folder}')

    def select_output_folder(self):
        self.output_folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if self.output_folder:
            self.output_label.setText(f'Selected folder: {self.output_folder}')

    def convert_file(self):
        output_format = self.format_combo.currentText()
        if not hasattr(self, 'output_folder'):
            self.status_label.setText('Please select an output folder.')
            return

        converter = None

        if self.image_file:
            converter = self.get_converter(self.image_file, output_format)
            output_file = self.get_output_file_path(self.image_file, output_format)
            if converter.convert(self.image_file, output_file):
                self.status_label.setText(f'File converted and saved to: {output_file}')
        elif self.image_folder:
            for filename in os.listdir(self.image_folder):
                image_file = os.path.join(self.image_folder, filename)
                converter = self.get_converter(image_file, output_format)
                output_file = self.get_output_file_path(image_file, output_format)
                if converter.convert(image_file, output_file):
                    self.status_label.setText(f'Files are converted and saved to: {self.output_folder}')

    def get_converter(self, file_path: str, output_format: str) -> ImageConverter:
        _, input_format = os.path.splitext(file_path)
        return ImageConverterFactory.get_converter(input_format)

    def get_output_file_path(self, input_path: str, output_format: str) -> str:
        image_name, _ = os.path.splitext(os.path.basename(input_path))
        output_file = f'{image_name}.{output_format}'
        return os.path.join(self.output_folder, output_file)

def main():
    app = QApplication(sys.argv)
    ex = ConverterApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()