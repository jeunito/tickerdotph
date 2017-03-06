from setuptools import setup

setup(
    name="tickerph",
    version="0.1",
    packages=["tickerdotph"],
    scripts=["bin/tickerdotph"],
    install_requires=[
        "vcrpy",
        "nose",
        "lxml",
        "cssselect"
    ]
)
