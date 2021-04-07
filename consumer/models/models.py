import uuid
from datetime import datetime
from typing import NamedTuple


class MonitoringLog(NamedTuple):
    id: uuid.UUID
    url: str
    http_status: int
    response_time: int  # in microseconds
    created_at: datetime
    matched_rules: list

    def to_insert_params(self):
        return str(self.id), self.url, self.http_status, self.response_time, str(self.created_at), self.matched_rules
