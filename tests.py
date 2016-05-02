
import re


from importd import d
d(no_atexit=True)

from smarturls import translate_regex, surl, url

assert url == surl


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
    "/<uuid:foo>/": (
        [
            "/21EC2020-3AEA-4069-A2DD-08002B30309D/",
            "/21EC20203AEA4069A2DD08002B30309D/"
        ],
        [
            "/21EC2020-3AEA-4069-A2DD_08002B30309D/",
            "/21EC2020-3AEA-4069-A2DD-08002B30309G/",
            "/21EC20203AEA4069A2DD08002B30309G/",
            "/asd/", "/acs_asd/"
        ]
    ),
    "/<base64:foo>/": (
        [
            "/21EC2020-3AEA-4069-A2DD-08002B30309D/",
            "/21EC20203AEA4069A2DD08002B30309D/",
            "/21EC20203AEA4069A2DD08002B30309D==/",
            "/21EC20203AEA4069A2DD08002B30309D=/",
            "/21EC20203a__EA4069A2DD08002B30309D/",
        ],
        [
            "/21EC20203AEA4069A2DD08002B30309D===/",
            "/21EC2020.3AEA-4069-A2DD-08002B30309D/",
            "/21EC20203,AEA4069A2DD08002B30309D/",
            "/21EC20203A+EA4069A2==DD08002B30309D/",
            "/21EC20203A EA4069A2DD08002B30309D/",
        ]
    ),
    "/<ekey:foo>/": (
        [
            "/21EC2020-3AEA-4069-A2DD-08002B30309D/",
            "/21EC20203AEA4069A2DD08002B30309D/",
            "/21EC20203AEA4069A2DD08002B30309D../",
            "/21EC20203AEA4069A2DD08002B30309D./",
            "/21EC20203a__EA4069A2DD08002B30309D/",
        ],
        [
            "/21EC20203AEA4069A2DD08002B30309D.../",
            "/21EC2020.3AEA-4069-A2DD-08002B30309D/",
            "/21EC20203,AEA4069A2DD08002B30309D/",
            "/21EC20203A+EA4069A2..DD08002B30309D/",
            "/21EC20203A EA4069A2DD08002B30309D/",
        ]
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


print("All {0} smarturls tests passed.".format(count))
