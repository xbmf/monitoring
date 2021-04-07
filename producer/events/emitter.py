from pymitter import EventEmitter

from config import config
from producer.producer import producer

MONITORING_LOG_CREATED = "monitoring_log_created"

ee = EventEmitter()


@ee.on(MONITORING_LOG_CREATED)
def publish_monitoring_log(data):
    producer.publish(data, config.KAFKA_TOPIC)
