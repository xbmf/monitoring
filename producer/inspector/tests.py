from unittest import TestCase

from events.emitter import ee, MONITORING_LOG_CREATED
from inspector.inspector import check_website, MonitoringLog


class CheckWebsiteTest(TestCase):
    def test_normal_website(self):
        @ee.once(MONITORING_LOG_CREATED)
        def website_result(monitoring_log: MonitoringLog):
            self.assertEqual(monitoring_log.url, "http://aiven.io")
            self.assertEqual(monitoring_log.http_status, 200)

        check_website("http://aiven.io", [])

    def test_unreachable_website(self):
        @ee.once(MONITORING_LOG_CREATED)
        def website_result(monitoring_log: MonitoringLog):
            self.assertEqual(monitoring_log.url, "http://aiven-not-working.io")
            self.assertEqual(monitoring_log.http_status, 0)
            self.assertEqual(monitoring_log.response_time, -1)

        check_website("http://aiven-not-working.io", [])

    def test_not_found_website(self):
        @ee.once(MONITORING_LOG_CREATED)
        def website_result(monitoring_log: MonitoringLog):
            self.assertEqual(monitoring_log.url, "https://aiven.io/this-url-is-not-found")
            self.assertEqual(monitoring_log.http_status, 404)

        check_website("https://aiven.io/this-url-is-not-found", [])

    def test_normal_website_with_regexp_rules(self):
        @ee.once(MONITORING_LOG_CREATED)
        def website_result(monitoring_log: MonitoringLog):
            self.assertEqual(monitoring_log.url, "https://aiven.io/")
            self.assertEqual(monitoring_log.http_status, 200)
            self.assertEqual(monitoring_log.matched_rules, ["<meta charSet"])

        check_website("https://aiven.io/", ["<meta charSet", "no-match-regexp"])
