from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='premutils',
    version='1.0',
    author='Prem Aseem Jain',
    author_email='premaseem',
    description='utils for python package',
    test_suite='nose.collector',
    install_requires=required,
    url='https://github.com/premaseem'
)
