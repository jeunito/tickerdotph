from setuptools import setup

setup(
    name="tickerph",
    version="0.1",
    packages=["tickerdotph"],
    entry_points={
        "console_scripts": [
            "tickerdotph = tickerdotph:main"
        ]
    },
    install_requires=[
        "vcrpy",
        "nose",
        "lxml",
        "cssselect"
    ]
)
