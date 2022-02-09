# setup.py

from setuptools import setup, find_packages

setup(
    name="click-demo",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        todov1=src.todov1:cli
        todov2=src.todov2:cli
    """,
)
