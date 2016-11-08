#!/usr/bin/env python
# coding: utf-8
from setuptools import setup


setup(
    name='change_finder',
    version='0.0.1',
    description='An implementation of the algorithm for detecting outliers and change points from time series data.',  # nopep8
    author='nel215',
    author_email='otomo.yuhei@gmail.com',
    url='https://github.com/nel215/change_finder',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    packages=['change_finder'],
    install_requires=[
        "numpy",
        "scipy",
    ],
    keywords=['machine learning'],
)
