#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="cold_silence",
    version="0.0.1",
    author="App Development and Such",
    author_email="appdevelopmentandsuch@gmail.com",
    url="https://github.com/firstlast/cold-silence",
    description="Generate Django projects sans boilerplate code.",
    long_description="Generate Django projects sans boilerplate code.",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=("tests",)),
    zip_safe=True,
)
