#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='plot_dots',
    version='1.0.0',
    description='plot dots on 2D plane',
    long_description=long_description,
    url='https://github.com/green-green-green/plot_dots',
    author='green-green-green',
    author_email='w6ok3i@gmail.com',
    license='MIT',
    # 実際に動かす時に依存関係にあるライブラリをinstallしてくれる
    install_requires=['matplotlib'],
    keywords='plot',
    packages=find_packages(exclude=('tests')),
    # # 今回コマンドを作ったのでconsole_scriptsを記述している
    # entry_points={
    #     "console_scripts": [
    #         "pydata=pydata.__init__:main",
    #     ],
    # },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)