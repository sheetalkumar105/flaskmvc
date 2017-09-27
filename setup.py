from setuptools import setup

setup(
    name='flaskblog',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)