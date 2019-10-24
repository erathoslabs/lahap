from typing import Tuple

from boto3 import Session

from ..services.s3 import S3


class Glue:
    def __init__(self, session: Session):
        self.session = session
        self.client = session.client("glue")

    def _split_s3_location(self, s3_location: str) -> Tuple[str, str]:
        """Split S3 location from string 's3://bucket/path' to 'bucket' and 'path'.

        Args:
            s3_location (str): S3 full location as 's3://bucket/path'

        Returns:
            str, str: S3 bucket and path divided
        """
        path_without_fs = s3_location.replace("s3://", "")
        paths = path_without_fs.split("/", 1)
        return paths[0], paths[1]

    def _get_table_location(self, database: str, table: str) -> str:
        """Retrieve Table S3 location full path.

        Args:
            database (str): catalog Database
            table (str): catalog Table

        Returns:
            str: S3 location full path
        """
        response = self.client.get_table(DatabaseName=database, Name=table)
        return response.get("Table").get("StorageDescriptor").get("Location")

    def truncate_table(self, database: str, table: str) -> None:
        """Delete all files under S3 prefix.

        Args:
            database (str): catalog Database
            table (str): catalog Table
        """
        s3_location = self._get_table_location(database=database, table=table)
        bucket, prefix = self._split_s3_location(s3_location)
        S3(self.session).delete_by_prefix(bucket=bucket, prefix=prefix)

    def drop_table(self, database: str, table: str) -> None:
        """Drop only table definitions (schema).

        Args:
            database (str): catalog Database
            table (str): catalog Table
        """
        self.client.delete_table(DatabaseName=database, Name=table)
