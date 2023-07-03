import os
import pytest
from typing import Dict


@pytest.fixture(scope="function")
def directories(tmp_path):
    os.mkdir(tmp_path / "src")
    os.mkdir(tmp_path / "tests")


@pytest.fixture(scope="function")
def config() -> Dict[str, str]:
    config = {
        "name": "pymilka",
        "version": "1.0.0",
        "author": "John Doe",
        "author_email": "john.doe@example.com",
        "description": "Project",
    }
    return config
