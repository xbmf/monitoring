from pathlib import Path

from config import DIR_RESOURCES


def load_data_fixture(filename: str):
    path = "{}/fixtures/{}".format(DIR_RESOURCES, filename)
    return Path(path).read_text()
