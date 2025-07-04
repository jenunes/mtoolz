#!/usr/bin/env python3
"""Setup file for mtools."""

import platform
import re
import sys

# try importing from setuptools, if unavailable use distutils.core
try:
    from setuptools import setup, find_packages

    python_requires='>=3.8'

    # Additional dependencies from requirements.txt that should be installed
    # for full mtools feature support. These are optional dependencies to
    # simplify the default install experience, particularly where a build
    # toolchain is required.
    base_extras_requires = ['python-dateutil>=2.8.2,<3.0.0']
    extras_requires = {
        "all": ['numpy>=1.21.6', 'matplotlib>=3.5.3,<4.0.0', 'pymongo>=4.3.2,<5.0.0',
                'psutil>=5.9.3,<6.0.0', 'packaging>=21.3'] + base_extras_requires,
        "mlaunch": ['pymongo>=4.3.2,<5.0.0', 'psutil>=5.9.3,<6.0.0', 'packaging>=21.3'] + base_extras_requires,
        "mlogfilter": base_extras_requires.copy(),
        "mloginfo": ['numpy>=1.21.6'] + base_extras_requires,
        "mplotqueries": ['numpy>=1.21.6', 'matplotlib>=3.5.3,<4.0.0'] + base_extras_requires,
        "mtransfer": ['pymongo>=4.3.2,<5.0.0', 'wiredtiger>=3.2.1'] + base_extras_requires,
    }

    install_requires = []
    
    try:
        import argparse
    except ImportError:
        install_requires.append('argparse')

    try:
        from collections import OrderedDict
    except ImportError:
        install_requires.append('ordereddict')

    packages = find_packages()
    kws = {'install_requires': install_requires}

except ImportError:
    from distutils.core import setup

    # find_packages not available in distutils, manually define packaging
    packages = ['mtools',
                'mtools.mlaunch',
                'mtools.mlogfilter',
                'mtools.mloginfo',
                'mtools.mplotqueries',
                'mtools.mtransfer',
                'mtools.test',
                'mtools.util',
                'mtools.mlogfilter.filters',
                'mtools.mplotqueries.plottypes',
                'mtools.mloginfo.sections']
    kws = {}

# import version from mtools/version.py
with open('mtools/version.py') as f:
    exec(f.read())

# read README.rst for long_description content
with open('README.rst') as f:
    long_description = f.read()

if sys.platform == 'darwin' and 'clang' in platform.python_compiler().lower():
    from distutils.sysconfig import get_config_vars
    res = get_config_vars()
    for key in ('CFLAGS', 'PY_CFLAGS'):
        if key in res:
            flags = res[key]
            flags = re.sub('-mno-fused-madd', '', flags)
            res[key] = flags

setup(
    name='mtoolz',
    version=__version__,
    packages=packages,
    entry_points={
        "console_scripts": [
            "mlaunch=mtools.mlaunch.mlaunch:main",
            "mlogfilter=mtools.mlogfilter.mlogfilter:main",
            "mloginfo=mtools.mloginfo.mloginfo:main",
            "mplotqueries=mtools.mplotqueries.mplotqueries:main",
            "mtransfer=mtools.mtransfer.mtransfer:main",
        ],
    },
    author='Jean Nunes',
    author_email='',
    url='https://github.com/jenunes/mtoolz',
    description=("Enhanced MongoDB diagnostic tools with MongoDB 4.4+ JSON log format support. "
                 "Useful scripts to parse and visualize MongoDB log files, "
                 "launch test environments, and reproduce issues."),
    long_description=long_description,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Database',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    keywords='MongoDB logs testing',
    extras_require=extras_requires,
    **kws
)
