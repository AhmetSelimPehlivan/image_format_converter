from setuptools import setup, find_packages

setup(
    name='image_converter',
    version='1.0.0',
    description='A PyQt5-based application to convert CR3, JPG, PNG, JPEG, and WEBP image formats.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'Pillow==9.4.0',
        'PyQt5==5.15.9',
        'mock'
    ],
    entry_points={
        'console_scripts': [
            'image_converter=image_converter.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
