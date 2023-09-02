from setuptools import setup, find_packages

setup(
    name='here-to-help',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # your dependencies
    ],
    entry_points = {
        'console_scripts': ['hth=here_to_help.cli:main'],
    }
)
