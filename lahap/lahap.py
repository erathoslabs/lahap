from pyathena.cursor import Cursor

COMPRESSION_FORMATS = {
    "PARQUET": ["UNCOMPRESSED", "SNAPPY", "LZO", "GZIP"],
    "ORC": ["UNCOMPRESSED", "SNAPPY", "ZLIB", "LZO", "GZIP"],
}


def create_table_from_query(
    cursor: Cursor,
    database: str,
    table: str,
    query: str,
    file_format: str,
    file_compression: str,
    external_location: str,
) -> None:
    """Creates a new table populated with the results of a SELECT query (CTA).

    Args:
        cursor (Cursor): PyAthena cursor
        database (str): target Glue catalog database
        table (str): target Glue catalog table
        query (str): select statement
        file_format (str): data format of query results ('PARQUET' or 'ORC')
        file_compression (str): data compression of file_format  ('UNCOMPRESSED',
            'SNAPPY', 'ZLIB', 'LZO', 'GZIP')
        external_location (str): s3 path of result files
    """
    sql = f"""
          CREATE TABLE {database}.{table}
          WITH (
                external_location = '{external_location}',
                format = '{file_format}',
                parquet_compression = '{file_compression}')
          AS {query};
          """
    cursor.execute(sql)
