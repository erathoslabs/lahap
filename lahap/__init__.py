import boto3

from .lahap import Lahap


def create_session(**kwargs) -> Lahap:
    session = boto3.Session(**kwargs)
    return Lahap(session=session)
