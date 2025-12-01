"""
Stock Analyzer Package Setup
"""

from setuptools import setup, find_packages

setup(
    name="stock-analyzer",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
)
