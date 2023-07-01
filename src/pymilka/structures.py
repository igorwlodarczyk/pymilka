import os
from pymilka.logger import logger
from pathlib import Path
from typing import Union


class Directory:
    def __init__(self, directory_name: str, path: Union = ""):
        self.directory_path = os.path.join(path, directory_name)
        os.mkdir(self.directory_path)


class ProjectFile:
    def __init__(self, file_name: str, directory: Union[Path, str] = ""):
        self.file_name = file_name
        self.file_path = os.path.join(directory, self.file_name)
        self.__create_file()

    def __create_file(self):
        with open(self.file_path, "w"):
            logger.debug(f"Successfully created {self.file_name}.")
