import re
from django.conf import settings
from django.conf.urls.defaults import url

REGEXERS = {
    "word": "\w+",
    "digit": "\d",
    "int": "\d+",
    "int2": "\d{2,2}",
    "int4": "\d{4,4}",
    "slug": "[\w-]+",
    "username": "[\w.@+-]+",
}
REGEXERS.update(getattr(settings, "SURL_REGEXERS", {}))
_R = re.compile("<((\w+:)?\w+)>")

def _regex_substituter(m):
    name = m.groups()[0]
    if ":" not in name: name = "word:%s" % name
    t, n = name.split(":")
    return "(?P<%s>%s)" % (n, REGEXERS[t])

def translate_regex(regex):
    if not regex.startswith("/"): return regex
    return "^%s$" % _R.sub(_regex_substituter, regex)[1:]

def surl(regex, *args, **kw):
    return url(translate_regex(regex), *args, **kw)
