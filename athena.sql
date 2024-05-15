CREATE EXTERNAL TABLE browsing_events (
    bank_name STRING,
    page_name STRING,
    customer_guid STRING,
    external_visitor_id STRING,
    login_state_name STRING,
    form_step_name STRING,
    adobe_fallback_id STRING,
    product_click_registration STRING,
    form_name STRING,
    cookie_consent_value STRING,
    page_sub_label STRING,
    page_id STRING,
    product_name STRING,
    load_dt_utc DATE
)  -- noqa: PRS
PARTITIONED BY (source_export_dttm STRING)  -- noqa: PRS
STORED AS PARQUET
LOCATION 's3://{bucket}/browsing_events/'