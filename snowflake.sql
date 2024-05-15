CREATE OR REPLACE TABLE parquet_col (
  custKey NUMBER DEFAULT NULL,
  orderDate DATE DEFAULT NULL,
  orderStatus VARCHAR(100) DEFAULT NULL,
  discount DECIMAL(4,2),
  price VARCHAR(255) COMMENT 'prince of the product'
);
