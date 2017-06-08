import nosewatch
from setuptools import setup, find_packages


setup(
    name='nose-watch',
    version=nosewatch.get_version(),
    author='Lukasz Balcerzak',
    author_email='lukaszbalcerzak@gmail.com',
    description=nosewatch.__doc__.strip(),
    url='https://github.com/lukaszb/nose-watch',
    packages=find_packages(),
    long_description=open('README.rst').read(),
    setup_requires=['nose>=1.0'],
    install_requires=['watchdog>=0.6'],
    tests_require=['mock'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Testing',
    ],
    entry_points={
        'nose.plugins.0.10': [
            'watch = nosewatch.plugin:WatchPlugin'
        ]
    }
)
