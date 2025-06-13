-- Set context
USE ROLE SNOWFLAKE_LEARNING_ROLE;
USE WAREHOUSE SNOWFLAKE_LEARNING_WH;
USE DATABASE SNOWFLAKE_LEARNING_DB;
SET schema_name = CONCAT(current_user(), '_LOAD_SAMPLE_DATA_FROM_S3');
USE SCHEMA IDENTIFIER($schema_name);

-- Create Stage pointing to S3
CREATE OR REPLACE STAGE blob_stage
URL = 's3://sfquickstarts/tastybytes/'
FILE_FORMAT = (TYPE = CSV);

-- Preview files in stage
LIST @blob_stage/raw_pos/menu/;

-- Load data from S3 into the MENU table
COPY INTO MENU
FROM @blob_stage/raw_pos/menu/
FILE_FORMAT = (TYPE = 'CSV');
