# Lahap

Lahap is a utility package for AWS Athena and AWS Glue.

<a href="https://github.com/psf/black"><img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Usage
In order to run Lahap functions you must instantiate a PyAthena cursor and use it as a parameter:
```python
from pyathena import connect
cursor = connect(
    aws_access_key_id="access_key_id",
    aws_secret_access_key="secret_acces_key",
    s3_staging_dir="s3://bucket/path/",
    region_name="us-east-1",
).cursor()
```

### Create table from query (CTA)
Creates a new table populated with the results of a SELECT query.
https://docs.aws.amazon.com/athena/latest/ug/create-table-as.html
```python
from lahap.lahap import create_table_from_query
create_table_from_query(
    cursor=cursor,
    database="database",
    table="table",
    query="SELECT * FROM sampledb.elb_logs",
    file_format="PARQUET",
    file_compression="GZIP",
    external_location="s3://bucket/path",
)
```
