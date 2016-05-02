from setuptools import setup

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ""

setup(
    name="smarturls",
    description="a url construction helper for django",
    long_description=long_description,

    version="0.1.6",
    author='Amit Upadhyay',
    author_email="upadhyay@gmail.com",

    url='http://amitu.com/smarturls/',
    license='BSD',

    py_modules=["smarturls"],

    zip_safe=True,

    install_requires=["Django>=1.5"],
)
