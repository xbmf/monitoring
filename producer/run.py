import asyncio

from helpers.resource import load_data_fixture
from inspector.inspector import check_website
from scheduler.scheduler import start_scheduler
from scheduler.schemas import WebsiteSchema

if __name__ == "__main__":
    websites = WebsiteSchema().loads(json_data=load_data_fixture("websites.json"), many=True)
    start_scheduler(websites, check_website)
