import os
import pytest


@pytest.fixture(scope="function")
def directories(tmp_path):
    os.mkdir(tmp_path / "src")
    os.mkdir(tmp_path / "tests")
