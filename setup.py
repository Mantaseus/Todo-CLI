import setuptools
import os.path

long_description = ''
if os.path.isfile("README.md"):
    with open("README.md", "r") as fh:
        long_description = fh.read()

setuptools.setup(
    name="todocli",
    version="0.2.1",
    author="Mantaseus",
    description = 'A module that installs a command line program to manage TODO lists',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'http://sys-ghar/gitea/mantaseus/todo_cli',
    license = 'MIT',

    packages = ['todocli'],
    entry_points = {
        'console_scripts': [
            'todo = todocli:run_main',
        ]
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'docopt',
        'tabulate',
    ],
)
