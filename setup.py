from setuptools import setup, find_packages

setup(
    name='analyserlib',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Sorting and recursion python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/BlankDevs/analyserlib',
    author='Wisani Baloyi',
    author_email='wisanibaloyi65@gmail.com'
)