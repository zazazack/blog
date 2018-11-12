from pathlib import Path
from setuptools import setup, find_packages

about = {}

here = Path(__file__).absolute().parent
long_description = here.joinpath('README.md')

setup(
    author_email='wilsonze@gmail.com',
    author='Zachary Wilson',
    description='Containerized flask application.',
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    long_description=long_description.read_text(),
    name='blog',
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    # version=about['VERSION'],
    zip_safe=False,
)
