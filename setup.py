from distutils.core import setup

setup(
    name='MiiCardConsumers',
    version='0.9.0',
    author='Paul O''Neill',
    author_email='info@miicard.com',
    packages=['MiiCardConsumers'],
    url='http://pypi.python.org/pypi/MiiCardConsumers/',
    license='LICENSE.txt',
    description='Wrapper around the miiCard API.',
    long_description=open('README.txt').read(),
    install_requires=[        
        "oauth2 >= 1.5.211"
    ],
)