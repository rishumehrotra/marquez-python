# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Marquez

    Marquez is an open source **metadata service** for the **collection**, **aggregation**, and **visualization** of a data ecosystem's metadata.  # noqa: E501
"""


from setuptools import find_packages, setup
from marquez_client.version import VERSION

NAME = "marquez-python"
VERSION = VERSION
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    python_requires='>3.5.0',
    version=VERSION,
    description="Marquez Python Client",
    author_email="",
    url="",
    keywords=["Marquez"],
    packages=find_packages(),
    install_requires=[
        "requests",
        "six"
    ],
    include_package_data=True,
    long_description="""\
    Marquez-Python is an open source library for building clients that
    interact with a running Marquez instance.
    """
)
