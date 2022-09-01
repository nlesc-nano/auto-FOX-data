#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit Auto-FOX/__version__.py
version = {}
with open(os.path.join(here, 'FOXdata', '__version__.py'), encoding='utf-8') as f:
    exec(f.read(), version)

with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name='Auto-FOX Data',
    version=version['__version__'],
    description='A repository with MD data used by the Auto-FOX tests.',
    long_description=readme + '\n\n',
    author='Bas van Beek',
    author_email='b.f.van.beek@vu.nl',
    url='https://github.com/nlesc-nano/auto-FOX-data',
    packages=[
        'FOXdata',
        'FOXdata.armc',
        'FOXdata.armcpt',
    ],
    package_dir={'FOXdata': 'FOXdata'},
    package_data={'FOXdata': [
        'armc/*.hdf5',
        'armc/*/*.xyz',
        'armc/*/*.dill',
        'armcpt/*.hdf5',
        'armcpt/*/*.xyz',
        'armcpt/*/*.dill',
        'py.typed',
    ]},
    include_package_data=True,
    license="GNU General Public License v3 or later",
    zip_safe=False,
    keywords=[
        'science',
        'chemistry',
        'python-3',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Typing :: Typed',
    ],
    python_requires='>=3.4',
    install_requires=[],
    extras_require={'test': [
        'pytest>=6.0',
        'h5py',
        'numpy',
        'assertionlib>=2.2.0',
        'pyyaml>=5.1',
        'Nano-Utils>=2.0',
    ]}
)
