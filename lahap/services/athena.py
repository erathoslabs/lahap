from time import sleep

from boto3 import Session

COMPRESSION_FORMATS = {
    "PARQUET": ["UNCOMPRESSED", "SNAPPY", "LZO", "GZIP"],
    "ORC": ["UNCOMPRESSED", "SNAPPY", "ZLIB", "LZO", "GZIP"],
}


class Athena:
    def __init__(self, session: Session):
        self.session = session
        self.client = session.client("athena")

    def convert_table_to_parquet(
        self,
        query_database: str,
        query_table: str,
        external_location: str,
        result_database: str,
        result_table: str,
        compression: str = "GZIP",
    ) -> None:
        sql = f"""
              CREATE TABLE {result_database}.{result_table}
              WITH (
                    external_location = '{external_location}',
                    format = 'PARQUET',
                    parquet_compression = '{compression}')
              AS SELECT * FROM {query_database}.{query_table};
              """
        self.run_query(query=sql)

    def run_query(self, query: str) -> None:
        response = self.client.start_query_execution(QueryString=query)
        query_execution_id = response["QueryExecutionId"]
        self.wait_query_result(query_execution_id)

    def wait_query_result(self, query_execution_id: str) -> None:
        state = "RUNNING"
        while state == "RUNNING":
            result = self.client.get_query_execution(
                QueryExecutionId=query_execution_id
            )
            state = result["QueryExecution"]["Status"]["State"]
            if state == "RUNNING":
                sleep(2)
            elif state == "SUCCEEDED":
                break
            else:
                # TODO: write nice exception
                raise Exception
