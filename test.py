import os
import unittest
import subprocess
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication
from image_converter import ConverterApp, CR3Converter, ImageFileConverter, ImageConverterFactory, ImageConverterHelper

class TestCR3Converter(unittest.TestCase):
    @patch('subprocess.run')
    def test_convert_success(self, mock_run):
        converter = CR3Converter()
        mock_run.return_value = MagicMock(check_returncode=lambda: 0)
        result = converter.convert('test.cr3', 'output.jpg')
        self.assertTrue(result)

    @patch('subprocess.run')
    def test_convert_failure(self, mock_run):
        converter = CR3Converter()
        mock_run.side_effect = subprocess.CalledProcessError(1, 'cmd')
        result = converter.convert('test.cr3', 'output.jpg')
        self.assertFalse(result)

class TestImageFileConverter(unittest.TestCase):
    @patch('image_converter.Image.open')
    @patch('image_converter.Image.save')
    def test_convert_success(self, mock_save, mock_open):
        converter = ImageFileConverter()
        mock_image = MagicMock()
        mock_open.return_value = mock_image
        result = converter.convert('test.jpg', 'output.jpg')
        mock_open.assert_called_once_with('test.jpg')
        mock_save.assert_called_once_with('output.jpg')
        self.assertTrue(result)

    @patch('image_converter.Image.open')
    def test_convert_failure(self, mock_open):
        converter = ImageFileConverter()
        mock_open.side_effect = Exception('File error')
        result = converter.convert('test.jpg', 'output.jpg')
        self.assertFalse(result)

class TestImageConverterFactory(unittest.TestCase):
    def test_get_cr3_converter(self):
        converter = ImageConverterFactory.get_converter('.cr3')
        self.assertIsInstance(converter, CR3Converter)

    def test_get_image_file_converter(self):
        converter = ImageConverterFactory.get_converter('.jpg')
        self.assertIsInstance(converter, ImageFileConverter)

class TestImageConverterHelper(unittest.TestCase):
    @patch('image_converter.Image.rotate')
    def test_check_image_orientation(self, mock_rotate):
        mock_image = MagicMock()
        mock_image._getexif.return_value = {274: 3}  # Simulate orientation EXIF data
        result = ImageConverterHelper.check_image_orientation(mock_image)
        mock_rotate.assert_called_once_with(180, expand=True)
        self.assertEqual(result, mock_image)

class TestConverterApp(unittest.TestCase):
    @patch('PyQt5.QtWidgets.QFileDialog.getOpenFileName')
    def test_select_file(self, mock_getOpenFileName):
        app = QApplication([])
        mock_getOpenFileName.return_value = ('test.jpg', 'Image Files (*.jpg)')
        converter_app = ConverterApp()
        converter_app.select_file()
        self.assertEqual(converter_app.image_file, 'test.jpg')

    @patch('PyQt5.QtWidgets.QFileDialog.getExistingDirectory')
    def test_select_folder(self, mock_getExistingDirectory):
        app = QApplication([])
        mock_getExistingDirectory.return_value = 'test_folder'
        converter_app = ConverterApp()
        converter_app.select_folder()
        self.assertEqual(converter_app.image_folder, 'test_folder')

    @patch('PyQt5.QtWidgets.QFileDialog.getExistingDirectory')
    def test_select_output_folder(self, mock_getExistingDirectory):
        app = QApplication([])
        mock_getExistingDirectory.return_value = 'output_folder'
        converter_app = ConverterApp()
        converter_app.select_output_folder()
        self.assertEqual(converter_app.output_folder, 'output_folder')

    @patch('image_converter.CR3Converter.convert')
    @patch('image_converter.ImageFileConverter.convert')
    def test_convert_file_cr3(self, mock_image_convert, mock_cr3_convert):
        app = QApplication([])
        converter_app = ConverterApp()
        converter_app.image_file = 'test.cr3'
        converter_app.output_folder = 'output_folder'
        converter_app.format_combo.setCurrentText('jpg')
        converter_app.convert_file()
        mock_cr3_convert.assert_called_once_with('test.cr3', os.path.join('output_folder', 'test.jpg'))

    @patch('image_converter.ImageFileConverter.convert')
    @patch('image_converter.CR3Converter.convert')
    def test_convert_file_image(self, mock_cr3_convert, mock_image_convert):
        app = QApplication([])
        converter_app = ConverterApp()
        converter_app.image_file = 'test.jpg'
        converter_app.output_folder = 'output_folder'
        converter_app.format_combo.setCurrentText('png')
        converter_app.convert_file()
        mock_image_convert.assert_called_once_with('test.jpg', os.path.join('output_folder', 'test.png'))

if __name__ == '__main__':
    unittest.main()