from setuptools import setup

setup(
    name='application',
    packages=['application', 'main'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)