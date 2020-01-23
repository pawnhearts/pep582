#!/usr/bin/env python
"""The setup script."""
from subprocess import check_call

from setuptools import setup, find_packages
from setuptools.command import develop, install

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = []

test_requirements = []

setup(
    author="robotnaoborot",
    author_email='robotnaoborot@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.8',
    ],
    description="implements pep582(adds __pypackages__ to PYTHONPATH) via patching site.py",
    entry_points={
        'console_scripts': [
            'pep582=pep582.patch:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pep582',
    name='pep582',
    packages=find_packages(include=['pep582']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pawnhearts/pep582',
    version='0.1.2',
    zip_safe=False,
)


class PostDevelopCommand(develop.develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        from pep582.patch import update_site_py
        update_site_py()


class PostInstallCommand(install.install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        from pep582.patch import update_site_py
        update_site_py()
