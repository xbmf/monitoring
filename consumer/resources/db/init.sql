CREATE TABLE IF NOT EXISTS monitoring_logs
(
      id                UUID PRIMARY KEY,
      url               VARCHAR(1000) NOT NULL,
      http_status       INTEGER NOT NULL,
      created_at        TIMESTAMP NOT NULL,
      response_time     INTEGER NOT NULL,
      matched_rules     VARCHAR[]
);

TRUNCATE monitoring_logs;