import pytest
import os
from pymilka.structures import ProjectFile


@pytest.mark.parametrize("file_name", ["setup.cfg", "pyproject.toml", ".gitignore"])
@pytest.mark.parametrize("directory", [None, "src", "tests"])
def test_project_file_init(tmp_path, file_name, directory, directories):
    if directory:
        expected_file_path = tmp_path / directory / file_name
        project_file = ProjectFile(file_name=file_name, directory=tmp_path / directory)
    else:
        expected_file_path = tmp_path / file_name
        project_file = ProjectFile(file_name=file_name, directory=tmp_path)
    assert os.path.exists(expected_file_path)
    assert project_file.file_path == str(expected_file_path)
