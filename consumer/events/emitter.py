import logging

from pymitter import EventEmitter

from persistance.repository import log_repository

MONITORING_LOG_RECEIVED = "monitoring_log_received"

ee = EventEmitter()

logger = logging.getLogger(__name__)


@ee.on(MONITORING_LOG_RECEIVED)
def save_monitoring_log(monitoring_log):
    logger.info("persisting monitoring log: {}".format(monitoring_log))
    log_repository.save(monitoring_log)
