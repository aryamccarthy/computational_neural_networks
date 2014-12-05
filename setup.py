try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Computational Neural Networks',
  'author': 'Arya McCarthy',
  'url': 'http://www.example.com/',
  'author_email': 'mccara24@gmail.com',
  'version': '0.1',
}

setup(**config)
