#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

from setuptools import setup, find_packages

setup(
    author="Martin Ueding",
    author_email="dev@martin-ueding.de",
    description="Type speed measurement.",
    license="GPL2",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python",

    ],
    name="type-speed",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'type-speed=type_speed:main',
        ],
    },
    install_requires=[
    ],
    url="https://github.com/martin-ueding/type-speed",
    download_url="http://martin-ueding.de/download/type-speed/",
    version="1.6.1",
)
