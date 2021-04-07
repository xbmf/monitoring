import uuid

from models.models import MonitoringLog
from models.serializers import MonitoringLogSchema
from persistance import IManager
from persistance.manager import PostgreDbManager


class MonitoringLogRepository:
    def __init__(self, db_manager: IManager):
        self.db_manager = db_manager

    def save(self, monitoring_log: MonitoringLog):
        query = """
            INSERT INTO monitoring_logs (id, url, http_status, response_time, created_at, matched_rules)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        return self.db_manager.execute_update(query, monitoring_log.to_insert_params())

    def get_by_id(self, id: uuid.UUID):
        query = """
            SELECT id, url, http_status, response_time, created_at, matched_rules
            FROM monitoring_logs
            WHERE id=%s
        """
        row = self.db_manager.read_one(query, (str(id),))
        return MonitoringLogSchema().load(data=row)


log_repository = MonitoringLogRepository(PostgreDbManager())
