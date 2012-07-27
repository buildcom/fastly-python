import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "fastly-python",
	version = "1.0.1",
	author = "Chris Zacharias",
	author_email = "chris@imgix.com",
	description = ("A Python client libary for the Fastly API."),
	license = "BSD",
	keywords = "fastly",
	url = "https://github.com/zebrafishlabs/fastly-python",
	packages=['fastly', 'tests'],
	long_description=read('README'),
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"License :: OSI Approved :: BSD License",
	],
)
