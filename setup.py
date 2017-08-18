from setuptools import setup
import os

exec(compile(
    open('sphinx_sitemap/version.py').read(), 'sphinx_sitemap/version.py', 'exec'))

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGELOG = open(os.path.join(here, 'CHANGELOG.md')).read()

setup(
    name='sphinx-sitemap',
    description='Sitemap generator for Sphinx',
    long_description=README + '\n\n' + CHANGELOG,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Documentation',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
      ],
    version=__version__,
    author='Jared Dillard',
    author_email='jared.dillard@gmail.com',
    install_requires=['six', 'sphinx >= 1.2'],
    url="https://github.com/jdillard/sphinx-sitemap",
    packages=['sphinx_sitemap'],
 )
