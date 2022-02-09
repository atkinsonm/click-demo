# setup.py

from setuptools import setup, find_packages

setup(
    name="click-demo",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "todov1 = todov1.todov1:cli",
            "todov2 = todov2.todov2:cli",
            "todov3 = todov3.todov3:cli",
            "todov4 = todov4.cli:cli",
        ]
    },
)
