from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='nis',
    version='1.0',
    author='Automation Integration',
    author_email='automation_integration@rackspace.COM',
    description='NIS API',
    test_suite='nose.collector',
    dependency_links=['http://10.10.161.9:8080/packages/'],
    install_requires=required,
    url='https://github.rackspace.com/AutomationIntegration/nis'
)
