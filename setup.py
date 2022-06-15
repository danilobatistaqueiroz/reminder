#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup


package_name = 'reminder'
filename = 'reminder/__init__.py'


def get_version():
    import ast

    with open(filename) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return ''


def get_requirements():
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()


setup(
    name=package_name,
    version=get_version(),
    install_requires=get_requirements(),
    author='Danilo Batista de Queiroz',
    author_email='danilobatistaqueiroz@gmail.com',
    description='Reminder',
    url='https://github.com/danilobatistaqueiroz/reminder',
    long_description=get_long_description(),
    packages=[package_name, 'bin'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'reminder = bin.reminder:main'
        ]
    },
    license='License :: OSI Approved :: MIT License',
)