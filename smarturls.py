# -*- coding: utf-8 -*-


import re

from django.conf import settings

try:
    from django.conf.urls.defaults import url as ourl
except ImportError:
    from django.conf.urls import url as ourl


REGEXERS = {
    "word": "\w+",
    "digit": "\d",
    "int": "\d+",
    "int2": "\d{2,2}",
    "int4": "\d{4,4}",
    "slug": "[\w-]+",
    "username": "[\w.@+-]+",
    "uuid": "[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}",
}
REGEXERS.update(getattr(settings, "SURL_REGEXERS", {}))
_R = re.compile("<((\w+:)?\w+)>")


def _regex_substituter(m):
    """Regular Expression susbtitutions."""
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
