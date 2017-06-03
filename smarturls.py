# -*- coding: utf-8 -*-


"""Smarturls an URL construction helper for Django."""


import re

from django.conf import settings

try:
    from django.conf.urls.defaults import url as ourl
except ImportError:
    from django.conf.urls import url as ourl


__license__ = "BSD"
__author__ = "Amit Upadhyay"
__url__ = "https://github.com/amitu/smarturls#smart-urls-for-django"


REGEXERS = {
    "word": "\w+",
    "digit": "\d",
    "int": "\d+",
    "int2": "\d{2,2}",
    "int4": "\d{4,4}",
    "slug": "[\w-]+",
    "username": "[\w.@+-]+",
    "uuid": "[A-Fa-f0-9]{8}-?[A-Fa-f0-9]{4}-?4[A-Fa-f0-9]{3}-?[89abAB][a-fA-F0-9]{3}-?[a-fA-F0-9]{12}",
    "base64": "[0-9a-zA-Z\-_]+={0,2}",
    "ekey": "[0-9a-zA-Z\-_]+\.{0,2}",
    "something": ".+",
    "anything": ".*",
}


REGEXERS.update(getattr(settings, "SURL_REGEXERS", {}))
_R = re.compile("<((\w+:)?\w+)>")


def _regex_substituter(m):
    """Regular Expression substitutions."""
    name = m.groups()[0]
    if ":" not in name:
        name = "word:%s" % name
    t, n = name.split(":")
    return "(?P<%s>%s)" % (n, REGEXERS[t])


def translate_regex(regex):
    """Translate the Regular Expressions."""
    return regex if not regex.startswith("/") else "^%s$" % _R.sub(
        _regex_substituter, regex)[1:]


def surl(regex, *args, **kw):
    """Smart URL callback function."""
    return ourl(translate_regex(regex), *args, **kw)


url = surl
