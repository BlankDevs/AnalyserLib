from setuptools import setup, find_packages

setup(
    name='analyserlib',
    version='1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='blank devs data science python functions package',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas', 'json', 'srsly'],
    url='https://github.com/BlankDevs/analyserlib',
    author='Wisani Baloyi',
    author_email='wisanibaloyi65@gmail.com'
)
