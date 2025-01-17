# from setuptools import setup
from distutils.core import setup

from Cython.Build import cythonize
import numpy

setup(
    name='hellinger-distance-criterion',
    version=0.1,
    url='github.com/EvgeniDubov/hellinger-distance-criterion',
    author='Evgeni Dubov',
    author_email='evgeni.dubov@gmail.com',
    ext_modules=cythonize('hellinger_distance_criterion.pyx', language_level = "3"),
    include_dirs=[numpy.get_include()]
)
