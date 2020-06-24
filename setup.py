from setuptools import setup

setup(
    name='pyServer',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)