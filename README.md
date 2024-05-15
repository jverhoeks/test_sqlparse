# test_sqlparse


DDL
```
/* Create the table */ CREATE TABLE "public"."my_table" ("field_one" VARCHAR(10) PRIMARY KEY, "field_two" INT NOT NULL, "field_three" TIMESTAMPTZ, 'test table' INT)
```
```
{'name': 'field_one', 'type': 'VARCHAR', 'quoted': False, 'length': 10, 'primary_key': True, 'nullable': True, 'default': False}
{'name': 'field_two', 'type': 'INT', 'quoted': False, 'primary_key': False, 'nullable': False, 'default': False}
{'name': 'field_three', 'type': 'TIMESTAMPTZ', 'quoted': False}
{'name': 'test table', 'type': 'INT', 'quoted': True}
```
DDL
```
CREATE OR REPLACE TABLE "parquet_col" ("custkey" DECIMAL DEFAULT NULL, "orderdate" DATE DEFAULT NULL, "orderstatus" VARCHAR(100) DEFAULT NULL, "price" VARCHAR(255))
```
```
{'name': 'custKey', 'type': 'DECIMAL', 'quoted': False, 'primary_key': False, 'nullable': True, 'default': True}
{'name': 'orderDate', 'type': 'DATE', 'quoted': False, 'primary_key': False, 'nullable': True, 'default': True}
{'name': 'orderStatus', 'type': 'VARCHAR', 'quoted': False, 'length': 100, 'primary_key': False, 'nullable': True, 'default': True}
{'name': 'price', 'type': 'VARCHAR', 'quoted': False, 'length': 255}
```
DDL
```
CREATE EXTERNAL TABLE "browsing_events" ("bank_name" TEXT, "page_name" TEXT, "customer_guid" TEXT, "external_visitor_id" TEXT, "login_state_name" TEXT, "form_step_name" TEXT, "adobe_fallback_id" TEXT, "product_click_registration" TEXT, "form_name" TEXT, "cookie_consent_value" TEXT, "page_sub_label" TEXT, "page_id" TEXT, "product_name" TEXT, "load_dt_utc" DATE) /* noqa: PRS */ LOCATION 's3://{s3_bucket_customer_profile}/browsing_events/' WITH (PARTITIONED_BY=("source_export_dttm" TEXT) /* noqa: PRS */, FORMAT=PARQUET)
```
```
{'name': 'bank_name', 'type': 'TEXT', 'quoted': False}
{'name': 'page_name', 'type': 'TEXT', 'quoted': False}
{'name': 'customer_guid', 'type': 'TEXT', 'quoted': False}
{'name': 'external_visitor_id', 'type': 'TEXT', 'quoted': False}
{'name': 'login_state_name', 'type': 'TEXT', 'quoted': False}
{'name': 'form_step_name', 'type': 'TEXT', 'quoted': False}
{'name': 'adobe_fallback_id', 'type': 'TEXT', 'quoted': False}
{'name': 'product_click_registration', 'type': 'TEXT', 'quoted': False}
{'name': 'form_name', 'type': 'TEXT', 'quoted': False}
{'name': 'cookie_consent_value', 'type': 'TEXT', 'quoted': False}
{'name': 'page_sub_label', 'type': 'TEXT', 'quoted': False}
{'name': 'page_id', 'type': 'TEXT', 'quoted': False}
{'name': 'product_name', 'type': 'TEXT', 'quoted': False}
{'name': 'load_dt_utc', 'type': 'DATE', 'quoted': False}
```