from boto3 import Session


class S3:
    def __init__(self, session: Session):
        self.client = session.resource("s3")

    def delete_by_prefix(self, bucket: str, prefix: str) -> None:
        """Delete all S3 files by prefix.

        Args:
            bucket (str): S3 Bucket name
            prefix (str): S3 prefix

        Returns:
            None: none
        """
        bucket = self.client.Bucket(bucket)
        bucket.objects.filter(Prefix=prefix).delete()
