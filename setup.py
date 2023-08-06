from setuptools import setup, find_packages
from version import VERSION

setup(
    name='tvDatafeed',
    version=VERSION,

    url='https://github.com/vaibhavkakodiya/tvdatafeed.git',
    author='vaibhav kakodiya',
    author_email='vaibhavkakodiya12345@gmail.com',

    py_modules=['TvDatafeed'],

    setup_requires=[
    'pandas',
    'websocket-client==1.3.1',
    'requests==2.31.0'
    ],

    install_requires=[
    'pandas',
    'websocket-client==1.3.1',
    'requests==2.31.0'
    ],

    packages=find_packages()
)