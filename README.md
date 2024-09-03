# Image Converter

![Image Converter Logo](https://via.placeholder.com/150)

**A PyQt5-based application to convert CR3, JPG, PNG, JPEG, and WEBP image formats with robust design principles.**

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Introduction

The **Image Converter** is a desktop application built with PyQt5 that allows users to convert image files from CR3 (Canon RAW) format to other common image formats such as JPG, PNG, JPEG, and WEBP. The application is designed following SOLID principles and best practice design patterns to ensure modularity, scalability, and maintainability.

---

## Features

- **Support for Multiple Formats:** Convert CR3 files to JPG, PNG, JPEG, and WEBP formats.
- **Batch Conversion:** Convert single files or entire folders containing multiple images.
- **Orientation Handling:** Automatically correct image orientation based on EXIF data.
- **User-Friendly Interface:** Intuitive GUI built with PyQt5 for seamless user experience.
- **Error Handling:** Comprehensive error messages to guide users in case of issues during conversion.
- **Modular Design:** Adheres to SOLID principles, making the codebase easy to maintain and extend.

---

## Technologies Used

### Programming Language

- **Python 3.8+**  
  ![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

### Libraries and Frameworks

- **PyQt5**  
  ![PyQt5 Logo](https://upload.wikimedia.org/wikipedia/commons/0/0e/PyQt_logo.svg)  
  A set of Python bindings for Qt libraries, enabling the creation of cross-platform GUI applications.

- **Pillow**  
  ![Pillow Logo](https://python-pillow.org/images/logo.svg)  
  The Python Imaging Library adds image processing capabilities to your Python interpreter.

- **ExifTool**  
  ![ExifTool Logo](https://exiftool.org/images/logo.png)  
  A platform-independent Perl library plus a command-line application for reading, writing, and editing meta information in a wide variety of files.

- **Subprocess (Standard Library)**  
  Utilized for running external commands and interacting with the operating system.

---

## Installation

### Prerequisites

- **Python 3.8 or higher**  
  Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).

- **ExifTool**  
  The application relies on ExifTool for handling CR3 file conversions.  
  - **macOS:** Install via Homebrew  
    ```bash
    brew install exiftool
    ```
  - **Windows:** Download from the [official website](https://exiftool.org/) and follow the installation instructions.
  - **Linux:** Install via package manager  
    ```bash
    sudo apt-get install exiftool
    ```

### Clone the Repository

```bash
git clone https://github.com/yourusername/image_converter.git
cd image_converter
```

### Install Dependencies
Alternatively, install the package using setup.py:
```
pip install .
```

## Usage
## Running the Application

After installing the dependencies, you can run the application using the following command:
```
python ConverterApp.py
```

## Application Interface

### Select Image File or Folder:
- Click on "Browse Image File" to select a single CR3 or other supported image file, or click on "Browse Images Folder" to select a folder containing multiple images.

### Select Output Folder:
- Click on "Browse Output Folder" to choose where the converted images will be saved.

### Select Output Format:
- Choose the desired output format (JPG, PNG, JPEG, WEBP) from the dropdown menu.

### Convert:
- Click the "Convert" button to start the conversion process. The status label will update with the progress and completion messages.

## Project Structure


- `image_converter/`: Contains the main application code.
- `converters.py`: Defines the converter classes adhering to SOLID principles.
- `helpers.py`: Utility functions for image processing.
- `main.py`: Entry point for the PyQt5 application.
- `tests/`: Contains unit tests for the application.
- `test_image_converter.py`: Comprehensive test suite covering all functionalities.
- `requirements.txt`: Lists all Python dependencies.
- `setup.py`: Configuration for packaging and distribution.
- `README.md`: This documentation.
- `LICENSE`: Licensing information.

## Testing

The project includes a suite of unit tests to ensure the reliability and correctness of the application. The tests cover all major components, including file conversion logic and the GUI.

### Running Tests

Navigate to the Project Directory:

```bash
cd image_format_converter
```

Run the Tests:
```
python -m unittest discover tests
```

## Test Coverage

- **CR3Converter/**: Ensures CR3 files are correctly converted using ExifTool.
- **ImageFileConverter/**: Validates conversion of standard image formats and orientation handling.
- **ImageConverterFactory/**: Confirms the correct converter is returned based on file extension.
- **ImageConverterHelper/**: Checks image orientation correction based on EXIF data.
- **ConverterApp/**: Tests the GUI components and integration of conversion functionalities.

## Contributing

Contributions are welcome! Please follow these steps to contribute to the project:

### Create a Feature Branch
``` git checkout -b feature/YourFeature```

### Commit Your Changes
``` git commit -m "Add your message" ```

### Push to the Branch
``` git push origin feature/YourFeature ```

## Acknowledgements

- `PyQt5`: For providing the robust framework to build the GUI.
- `Pillow`: For powerful image processing capabilities.
- `ExifTool`: For handling metadata and CR3 file conversions.
- `SOLID Principles`: For guiding the design and architecture of the application

## Contact

For any questions or suggestions, feel free to reach out:

- `Author`: Ahmet Selim Pehlivan
- `Email`: ahmetselimpehlivan@gmail.com
- `GitHub`: [ahmetselimpehlivan](https://github.com/AhmetSelimPehlivan)