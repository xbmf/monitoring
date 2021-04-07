import logging

from kafka import KafkaProducer
from marshmallow import Schema, fields

from config import config
from producer import IProducer

logger = logging.getLogger(__name__)


class MonitoringLogSchema(Schema):
    url = fields.URL()
    http_status = fields.Int()
    response_time = fields.Int()
    created_at = fields.DateTime()
    matched_rules = fields.List(fields.Str())


class ProducerKafka(IProducer):
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
            security_protocol="SASL_SSL",
            sasl_mechanism="PLAIN",
            sasl_plain_username=config.KAFKA_USERNAME,
            sasl_plain_password=config.KAFKA_PASSWORD,
            ssl_cafile="ca.pem",
        )

    def publish(self, message, topic):
        message_str = MonitoringLogSchema().dumps(message)
        logger.info("publishing message: {}".format(message_str))
        try:
            self.producer.send(topic, value=bytes(message_str, "utf-8"))
        except Exception as err:
            logger.error("error while publishing message", err)
            raise err


producer = ProducerKafka()
