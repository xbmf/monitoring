import logging
import os
from os import path

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")

DIR_PROJECT = path.dirname(__file__)
DIR_RESOURCES = "{}/{}".format(DIR_PROJECT, "resources")


def init_loggers(log_level):
    root_logger = logging.getLogger("")
    root_logger.setLevel(log_level)

    console = logging.StreamHandler()
    formatter = logging.Formatter("PRODUCER: %(asctime)s %(name)-12s: %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    root_logger.addHandler(console)


class ConsumerConfig:
    ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
    KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "monitor_logs")
    KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    KAFKA_USERNAME = os.environ.get("KAFKA_USERNAME")
    KAFKA_PASSWORD = os.environ.get("KAFKA_PASSWORD")
    LOG_LEVEL = logging.INFO

    def __init__(self):
        init_loggers(self.LOG_LEVEL)


class TestConfig(ConsumerConfig):
    ENVIRONMENT = "test"
    KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "monitor_logs_test")
    LOG_LEVEL = logging.ERROR


if ENVIRONMENT == "test":
    config = TestConfig()
else:
    config = ConsumerConfig()
