"""robothead module installation script

robotheaad is a module used to control a servo-actuated face using PCA9685 i2c
controllers.
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='robothead',
    version='0.1.0',
    description='robotheaad PCA9685 servo-actuated face control', 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rmedinaday/robothead',
    #author='',
    #author_email='',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="robotics, pca9685, servo",
    packages=['robothead',],
    python_requires=">=3.8, <4",
    install_requires=['PyYAML'],
    license='MIT',
)

