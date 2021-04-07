from unittest.case import TestCase

from scheduler.scheduler import start_scheduler
from scheduler.schemas import WebsiteSchema


class SchedulerTest(TestCase):
    def test_scheduler_initialize(self):
        test_website = WebsiteSchema().load(
            data={"url": "https://aiven.io", "interval": 1, "regexp_rules": ["some-rule"]}
        )

        def mock_check_website(url, regexp_rules):
            pass

        schedule_manager = start_scheduler([test_website], mock_check_website)
        jobs = schedule_manager.get_jobs()
        self.assertEqual(jobs[0].id, test_website.get("url"))
