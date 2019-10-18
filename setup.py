from distutils.core import setup

from setuptools import find_packages

setup(
    name="Lahap",
    version="0.0.2",
    packages=find_packages(),
    url="https://github.com/erathoslabs/lahap",
    license="MIT",
    author="Erathos",
    author_email="heron@erathos.com",
    description="Utility package to AWS Athena and AWS Glue.",
    install_requires=["boto3"],
)
