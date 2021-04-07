import uuid
from datetime import datetime

from marshmallow import Schema, fields, post_load

from models.models import MonitoringLog


class ExtendedDateTimeField(fields.DateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, datetime):
            return value
        return super()._deserialize(value, attr, data, **kwargs)


class MonitoringLogSchema(Schema):
    id = fields.UUID(missing=uuid.uuid4)
    url = fields.URL()
    http_status = fields.Int()
    response_time = fields.Int()
    created_at = ExtendedDateTimeField()
    matched_rules = fields.List(fields.Str())

    @post_load
    def to_model(self, data, **kwargs):
        return MonitoringLog(
            id=data.get("id"),
            url=data.get("url"),
            http_status=data.get("http_status"),
            response_time=data.get("response_time"),
            created_at=data.get("created_at"),
            matched_rules=data.get("matched_rules"),
        )
