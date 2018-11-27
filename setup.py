from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read().strip()

setup(
    author_email='wilsonze@gmail.com',
    author='Zachary Wilson',
    description='Containerized flask application.',
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=['setuptools_scm', 'setuptools_scm_about'],
    use_scm_version={'write_to': 'blog/_version.py'},
    license='GPLv3',
    long_description=long_description,
    name='blog',
    packages=find_packages(),
    zip_safe=False,
    url='https://github.com/zazazack/blog',
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Other Scripting Engines',
        'Programming Language :: PL/SQL',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
)
