from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from config import config


class SchedulerManager:
    def __init__(self):
        if config.ENVIRONMENT == "test":
            self.scheduler = BackgroundScheduler()
        else:
            self.scheduler = BlockingScheduler()

    def init(self, websites, func):
        self.scheduler.configure(timezone="utc")
        for website in websites:
            self.scheduler.add_job(
                func,
                "interval",
                seconds=website.get("interval"),
                id=website.get("url"),
                kwargs={"url": website.get("url"), "regexp_rules": website.get("regexp_rules")},
            )

        self.scheduler.start()

    def get_jobs(self):
        return self.scheduler.get_jobs()


scheduler = SchedulerManager()


def start_scheduler(websites, func):
    scheduler.init(websites, func)
    return scheduler
