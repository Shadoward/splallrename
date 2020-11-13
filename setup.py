# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_namespace_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

install_requires = [
    'argparse',
    'numpy',
    'pandas',
    'glob',
    'tqdm',
]

extras_require = {
    'build' : [
        'setuptools',
    ],
    'tests' : [],
}

setup(
    name='nelallrename',
    version='0.2.0',
    description='Rename *.ALL using *.NEL group LineRunline',
    long_description=readme,
    author='Patrice Ponchant',
    author_email='patrice.ponchant@furgo.com',
    include_package_data = True,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=extras_require['tests'],
    url='',
    license=license,
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    keywords='NEL ALL Konsgberg Rename',
    classifiers=[
        'Development Status :: 2 - Beta',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering'
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

