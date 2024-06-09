# setup.py
from setuptools import setup, find_packages

setup(
    name="utilkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            # Если хотите создать консольный скрипт
        ],
    },
    author="Ваше Имя",
    author_email="your.email@example.com",
    description="A utility library for various scripts",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/utilkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
