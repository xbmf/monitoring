from pathlib import Path

from config import DIR_RESOURCES


def load_db_resource(filename: str):
    path = "{}/db/{}".format(DIR_RESOURCES, filename)
    return Path(path).read_text()
