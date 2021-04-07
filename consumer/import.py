from helpers.resource import load_db_resource
from persistance.manager import PostgreDbManager

if __name__ == "__main__":
    db_manager = PostgreDbManager()
    db_manager.clean(load_db_resource("init.sql"))
