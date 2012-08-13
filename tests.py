from importd import d
d(no_atexit=True)
from smarturls import translate_regex
import re

TESTS = {
    "/<int:foo>/": (
        ["/123/", "/123123123123123/", "/1/"],
        ["/123", "/asd/", "/12/3/", "/123.123/", "/123a/"]
    ),
    "/<int2:foo>/": (
        ["/12/", "/01/"],
        ["/123/", "/123", "/asd/", "/123.123/", "/123a/"]
    ),
    "/<int4:foo>": (
        ["/0000", "/0122"],
        ["/1234/", "/123", "/asd/", "/123.123/", "/123a/"]
    ),
    "/<word:foo>/": (
        ["/asd/", "/123/", "/a/"],
        ["/as-d/", "/asd.d/", "/asd"]
    ),
    "/<digit:foo>/": (
        ["/1/", "/0/"],
        ["/123/", "/12/", "/1", "/123", "/asd/", "/123.123/", "/123a/"]
    ),
    "/<slug:foo>/": (
        ["/asd/", "/123/", "/a/", "/asd-123/", "/asd-qwe-123---/"],
        ["/as-d", "/asd.d/", "/asd", "/asd.txt/"]
    ),
    "/<username:foo>/": (
        [
            "/asd/", "/123/", "/---/", "/john.doe/",
            "/amitu@foo/", "/ami+foo@gmail.com/"
        ], ["/asd", "/asd%20/"]
    ),
}
TESTS["/<foo>/"] = TESTS["/<word:foo>/"]

count = 0
for pattern in TESTS:
    passing, failing = TESTS[pattern]
    patternt = translate_regex(pattern)
    patternc = re.compile(patternt)
    for url in passing:
        assert patternc.match(url[1:]), "p: %s %s %s" % (
            url, pattern, patternt
        )
        count += 1
    for url in failing:
        assert not patternc.match(url[1:]), "f: %s %s %s" % (
            url, pattern, patternt
        )
        count += 1

print "All %s smarturls tests passed." % count

