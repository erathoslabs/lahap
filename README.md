# Lahap
Lahap is a utility package for AWS Athena and AWS Glue.

<a href="https://github.com/psf/black"><img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Usage
In order to run Lahap functions you must instantiate a Lahap session, a `boto3.Session` wrapper to manage boto3 calls. Use can provide any valid `boto3.Session` parameter to it.
```python
from lahap import create_session

lahap = create_session(region_name="us-east-1", profile_name="profile") # using profile
lahap = create_session(region_name="us-east-1", aws_access_key_id="access-key", 
                       aws_secret_access_key="secret-key") # using explicit key credentials
```

### Truncate table
Deletes all S3 files located in a Glue Table's S3 location. Be careful.
```python
lahap.truncate_table(database="catalog-database", table="catalog-table")
```

### Drop table
Drops Glue Table with or without its respective data in S3. Be careful.
```python
lahap.drop_table(database="catalog-database", table="catalog-table", only_schema=False)
```

### Convert table to Parquet
Copies a table storing it as Parquet files through CTA.
```python
lahap.convert_table_to_parquet(
    query_database="source-database",
    query_table="source-table",
    compression="parquet-compression", # "UNCOMPRESSED", "SNAPPY", "LZO", "GZIP"
    result_database="result-database",
    result_table="result-table-parquet",
    external_location="s3://my-bucket/path",
)
```

### Convert query to Parquet
Create a new table from query and storing it as Parquet files through CTA.
```python
lahap.convert_query_to_parquet(
    query="SELECT * FROM database.table",
    compression="parquet-compression", # "UNCOMPRESSED", "SNAPPY", "LZO", "GZIP"
    result_database="result-database",
    result_table="result-table-parquet",
    external_location="s3://my-bucket/path",
)
```

##References
###Amazon Athena CTA
https://docs.aws.amazon.com/athena/latest/ug/create-table-as.html