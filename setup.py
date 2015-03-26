from setuptools import setup


setup(
    name="shutit",
    version="0.7.0",
    url='https://github.com/ianmiell/shutit',
    description='Complex and Dynamic Docker Builds Made Simple',
    author='Ian Miell',
    install_requires=[
        'pexpect>=2.0,<3.0',
        'bottle>=0.1',
        'pynsca>=1.5',
        'manhole>=0.1',
        'texttable>=0.1',
    ],
    packages=['shutit'],
    entry_points={
        'console_scripts': [
            'shutit = shutit.shutit_main:shutit_main',
        ],
    },
    license="http://opensource.org/licenses/MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
