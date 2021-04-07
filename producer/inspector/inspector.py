import re
from datetime import datetime
from typing import NamedTuple

import requests

from events.emitter import ee, MONITORING_LOG_CREATED


class MonitoringLog(NamedTuple):
    url: str
    http_status: int
    response_time: int
    created_at: datetime
    matched_rules: list


def check_website(url: str, regexp_rules: list):
    request_date = datetime.now()
    response = None
    matched_rules = []
    try:
        response = requests.get(url)
        http_status = response.status_code
        response_time = response.elapsed.microseconds
    except requests.exceptions.RequestException as e:
        http_status = 0
        response_time = -1

    if response:
        content = response.text
        for regexp_rule in regexp_rules:
            if bool(re.search(regexp_rule, content)):
                matched_rules.append(regexp_rule)

    ee.emit(
        MONITORING_LOG_CREATED,
        MonitoringLog(
            url=url,
            http_status=http_status,
            response_time=response_time,
            created_at=request_date,
            matched_rules=matched_rules,
        ),
    )
