from setuptools import setup

from tvDatafeed import __version__

setup(
    name='tvDatafeed',
    version=__version__,

    url='https://github.com/vaibhavkakodiya/tvdatafeed.git',
    author='vaibhav kakodiya',
    author_email='vaibhavkakodiya12345@gmail.com',

    py_modules=['TvDatafeed'],

    install_requires=[
    'returns-decorator',
    'pandas',
    'websocket-client==1.3.1',
    'requests==2.31.0'
],
)