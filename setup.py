from setuptools import setup

setup(
    name = "django-surl",
    description = "a url construction helper for django",
    long_description=open('README.rst', 'rt').read(),

    version = "0.1.0",
    author = 'Amit Upadhyay',
    author_email = "upadhyay@gmail.com",

    url = 'http://amitu.com/django-surl/',
    license = 'BSD',

    py_modules = ["django_surl"],

    zip_safe = True,
)
