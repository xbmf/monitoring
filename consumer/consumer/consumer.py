import logging

from kafka import KafkaConsumer

from config import config
from consumer import IConsumer
from events.emitter import ee, MONITORING_LOG_RECEIVED
from models.serializers import MonitoringLogSchema

logger = logging.getLogger(__name__)


class ConsumerKafka(IConsumer):
    def __init__(self, topic):
        self.consumer = KafkaConsumer(
            topic,
            group_id="monitoring",
            bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
            auto_offset_reset="earliest",
            consumer_timeout_ms=1000,
            security_protocol="SASL_SSL",
            sasl_mechanism="PLAIN",
            ssl_cafile="ca.pem",
            sasl_plain_username=config.KAFKA_USERNAME,
            sasl_plain_password=config.KAFKA_PASSWORD,
        )
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            logger.info("checking new messages...")
            for message in self.consumer:
                logger.info("consumed message: {}".format(message.value))
                monitoring_log = MonitoringLogSchema().loads(message.value)
                ee.emit(MONITORING_LOG_RECEIVED, monitoring_log)
            self.consumer.commit()

    def stop(self):
        self.running = False


consumer = ConsumerKafka(config.KAFKA_TOPIC)
