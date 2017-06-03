# -*- coding: utf-8 -*-

from setuptools import setup

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ""


setup(
    name="smarturls",
    description="A URL construction helper for Django.",
    long_description=long_description,

    version="0.1.8",
    author='Amit Upadhyay',
    author_email="upadhyay@gmail.com",

    url='https://amitu.com/smarturls/',
    license='BSD',

    py_modules=["smarturls"],

    zip_safe=True,

    install_requires=["Django>=1.5"],

    tests_require=['tox'],

    keywords=['helper', 'django', 'utils', 'regex', 'utility'],

    classifiers=[

        'Intended Audience :: Developers',

        'Natural Language :: English',

        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',

        'Programming Language :: Python :: Implementation :: CPython',

        'Topic :: Software Development',

    ],
)
