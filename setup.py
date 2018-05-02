from setuptools import setup, find_packages

setup(
    name='dukedoms-player-service-tests',
    version='0.0.0',
    description='containerized testing environment for dukedoms player service',
    packages=find_packages(exclude=['&.tests']),
    install_requires=[
        'addict',
        'behave',
        'bravado',
        'sqlalchemy',
        'psycopg2',
        'pyhamcrest'
    ]
)
