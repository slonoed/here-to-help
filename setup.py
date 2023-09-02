from setuptools import setup, find_packages

setup(
    name='here_to_help',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hth = here_to_help.cli:main',
        ],
    },
)