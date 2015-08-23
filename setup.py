import os
import sys
from setuptools import setup

install_requires = []
tests_require = ["unittest2"]

base_dir = os.path.dirname(os.path.abspath(__file__))

version = "0.0.1"

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'v%s'" % (version, version))
    os.system("python setup.py sdist bdist_wheel upload -r pypi")
    print("Published version %s, do `git push --tags` to push new tag to remote" % version)
    sys.exit()

if sys.argv[-1] == 'syncci':
    os.system("panci --to=tox .travis.yml > tox.ini");
    sys.exit();

setup(
    name = "pycat",
    version = version,
    url = "https://github.com/wookay/pycat",
    packages = ["pycat"],
    zip_safe = False,
    install_requires = install_requires,
    tests_require = tests_require,
    test_suite = "tests.get_tests",
)
