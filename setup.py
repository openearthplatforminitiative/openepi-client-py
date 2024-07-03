from setuptools import find_packages, setup

__version__ = "0.1.11"

setup(
    name="openepi-client",
    packages=find_packages(),
    version=__version__,
    description="A python library for interacting with the OpenEPI data",
)
