from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read().strip()

with open(path.join(here, 'blog', 'VERSION'), encoding='utf-8') as f:
    __version__ = f.read().strip()


setup(
    author_email='wilsonze@gmail.com',
    author='Zachary Wilson',
    description='Containerized flask application.',
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    long_description=long_description,
    name='blog',
    packages=find_packages(),
    # use_scm_version=True,
    # setup_requires=['setuptools_scm'],
    version=__version__,
    zip_safe=False,
)
