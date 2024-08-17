# setup.py
from setuptools import setup, find_packages

setup(
    name="scriputils",
    version="0.2.3",
    packages=find_packages(),
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [],
    },
    author="Yuriy Simonov",
    author_email="simonovyup@gmail.com",
    description="A utility library for various scripts",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/utilkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
