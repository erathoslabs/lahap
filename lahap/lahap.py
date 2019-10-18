from boto3 import Session

from .services.athena import Athena
from .services.glue import Glue


class Lahap:
    def __init__(self, session: Session):
        self.session = session

    def convert_table_to_parquet(
        self,
        query_database: str,
        query_table: str,
        external_location: str,
        result_database: str,
        result_table: str,
        compression: str = "GZIP",
    ) -> None:
        """Convert S3 Table data to Parquet format.

        Args:
            query_database (str): source catalog Database of query_table
            query_table (str): source catalog Table to be converted
            external_location (str): S3 location to store converted Table data
            result_database (str): catalog Database used to store new Table
            result_table (str): new catalog Table to be created
            compression (str): Parquet compression format ('UNCOMPRESSED', 'SNAPPY',
                'LZO', 'GZIP'), default is 'GZIP'

        Returns:
            None: none
        """
        Athena(self.session).convert_table_to_parquet(
            query_database=query_database,
            query_table=query_table,
            compression=compression,
            result_database=result_database,
            result_table=result_table,
            external_location=external_location,
        )

    def truncate_table(self, database: str, table: str) -> None:
        """Delete all files from Athena table location in S3.

        Args:
            database (str): target Glue catalog database
            table (str): target Glue catalog table

        TODO: add catalog_id parameter
        """
        Glue(self.session).truncate_table(database=database, table=table)
