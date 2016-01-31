from fabric.api import local, cd


def docs():
    local("./bin/docs")
    local("./bin/python3 setup.py upload_sphinx --upload-dir=docs/html")


def release():
    # update version id in setup.py, changelog and docs/source/conf.py
    local("python3 setup.py bdist_egg sdist --formats=bztar,gztar,zip upload")
