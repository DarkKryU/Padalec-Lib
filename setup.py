from setuptools import setup, find_packages

setup(
    name='padaleclib',
    version='0.0.1',
    author='Dark KryU',
    description='A small library with some useful tools',

    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Development Status :: Early Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12.0',
    ],
)
