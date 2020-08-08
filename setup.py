import re
from setuptools import setup, find_packages
from codecs import open
from os import path
import versioneer

setup(
    name="fantastic-bump",
    description="fantastic-bump",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(), 
    long_description="fantastic-bump",
    url="https://github.com/glasnt/fantastic-bump",
    author="Katie McLaughlin",
    author_email="katie@glasnt.com",
    license="New BSD",
)
