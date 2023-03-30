from __future__ import with_statement

from setuptools import setup
import sys


def get_version():
    with open("ring/__version__.py") as f:
        empty, version = f.read().split("__version__ = ")
    assert empty == ""
    version = version.strip().strip("\"'")
    assert version.startswith("0.")
    return version


install_requires = [
    "six>=1.11.0",
    "wirerope>=0.4.7",
    "attrs>=19.3.0",
    'inspect2>=0.1.0;python_version<"3.0.0"',
    'functools32>=3.2.3-2;python_version<"3.0"',
]
tests_require = [
    "pytest>=3.10.1",
    "pytest-cov",
    "pytest-lazy-fixture>=0.6.2",
    "mock",
    "patch",
    "pymemcache",
    "redis;python_version<'3.0'",
    "redis>=4.2.0;python_version>='3.0'",
    "requests",
    "diskcache>=4.1.0",
    "django<4",
    "numpy",
]
docs_require = [
    "sphinx",
    "django",
]

try:
    import __pypy__  # noqa
except ImportError:
    # CPython-only
    tests_require.extend(
        [
            "pylibmc",
        ]
    )

# new feature support
if (3, 3) <= sys.version_info:
    if sys.version_info < (3, 5):
        assert tests_require[0].startswith("pytest")
        tests_require[0] = "pytest==3.10.1"
        tests_require.append("pytest-asyncio==0.5.0")
    else:
        tests_require.append("pytest-asyncio")
    tests_require.extend(
        [
            "aiomcache",
        ]
    )

if sys.version_info[0] == 2:
    tests_require.extend(
        [
            "python-memcached",
        ]
    )
else:
    tests_require.extend(
        [
            "python3-memcached",
        ]
    )


dev_require = tests_require + docs_require


def get_readme():
    try:
        with open("README.rst") as f:
            return f.read().strip()
    except IOError:
        return ""


setup(
    name="ring",
    version=get_version(),
    description="Function-oriented cache interface with built-in memcache "
    "& redis + asyncio support.",
    long_description=get_readme(),
    author="Jeong YunWon",
    author_email="ring@youknowone.org",
    url="https://github.com/youknowone/ring",
    packages=(
        "ring",
        "ring/func",
    ),
    package_data={},
    install_requires=install_requires,
    tests_require=tests_require + ["tox", "tox-pyenv"],
    extras_require={
        "tests": tests_require,
        "docs": docs_require,
        "dev": dev_require,
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)  # noqa
