from setuptools import setup, find_packages

setup(
    name='application',
    packages=['main'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)