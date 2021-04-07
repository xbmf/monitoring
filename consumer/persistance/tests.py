import logging
from datetime import datetime
from unittest import TestCase

from helpers.resource import load_db_resource
from models.serializers import MonitoringLogSchema
from persistance.manager import PostgreDbManager
from persistance.repository import MonitoringLogRepository

logger = logging.getLogger()


class DbTest(TestCase):
    def setUp(self) -> None:
        self.db_manager = PostgreDbManager()
        self.db_manager.clean(load_db_resource("init.sql"))


class MonitoringLogRepositoryTest(DbTest):
    def test_save(self):
        log = MonitoringLogSchema().load(
            {
                "url": "https://aiven.io",
                "http_status": 200,
                "response_time": 1000,
                "created_at": str(datetime.utcnow()),
                "matched_rules": [],
            }
        )
        repository = MonitoringLogRepository(self.db_manager)
        repository.save(log)
        inserted = repository.get_by_id(log.id)
        self.assertEqual(inserted.id, log.id)
        self.assertEqual(inserted.url, log.url)
        self.assertEqual(inserted.http_status, log.http_status)
        self.assertEqual(inserted.created_at, log.created_at)
