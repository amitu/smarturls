from setuptools import setup

setup(
    name = "smarturls",
    description = "a url construction helper for django",
    long_description=open('README.rst', 'rt').read(),

    version = "0.1.1",
    author = 'Amit Upadhyay',
    author_email = "upadhyay@gmail.com",

    url = 'http://amitu.com/smarturls/',
    license = 'BSD',

    py_modules = ["smarturls"],

    zip_safe = True,
)
