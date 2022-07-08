"""
    Ory Keto API

    Documentation for all of Ory Keto's REST APIs. gRPC is documented separately.   # noqa: E501

    The version of the OpenAPI document: v0.8.0-alpha.2
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "forestvpn-ory-keto-client"
VERSION = "v0.8.0-alpha.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Ory Keto API",
    author="OpenAPI Generator community",
    author_email="hi@ory.sh",
    url="https://github.com/forestvpn/ory-keto-client-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Ory Keto API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    Documentation for all of Ory Keto&#39;s REST APIs. gRPC is documented separately.   # noqa: E501
    """
)
