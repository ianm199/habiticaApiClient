from setuptools import setup, find_packages

setup(
    name='habiticaApiClient',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description='An API Client for the Habit RPG Habitica. Not official',
    install_requires=[
        'requests',
    ],
)
