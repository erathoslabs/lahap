import pathlib
from distutils.core import setup

from setuptools import find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name="Lahap",
    version="0.1",
    packages=find_packages(),
    url="https://github.com/erathoslabs/lahap",
    license="MIT",
    author="Erathos",
    author_email="heron@erathos.com",
    description="Utility package to AWS Athena and AWS Glue.",
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=["boto3"],
)
