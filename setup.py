from setuptools import setup

try:
    long_description=open('README.rst', 'rt').read()
except Exception:
    long_description=""

setup(
    name = "smarturls",
    description = "a url construction helper for django",
    long_description=long_description,

    version = "0.1.2",
    author = 'Amit Upadhyay',
    author_email = "upadhyay@gmail.com",

    url = 'http://amitu.com/smarturls/',
    license = 'BSD',

    py_modules = ["smarturls"],

    zip_safe = True,
)
