from setuptools import setup

with open('README.md','r') as f:
    long_description = f.read()

with open('LICENSE','r') as f:
    license = f.read()

setup(name='cerberus',
      version='0.1.0',
      description='Lightweight security app',
      long_description=long_description,
      license=license,
      author='Alexandros Ntigkaris',
      url='https://github.com/ntigkaris/cerberus',
      packages=['cerberus'],
      python_requires='>=3.9.2',
      install_requires=['numpy','opencv-python'])
