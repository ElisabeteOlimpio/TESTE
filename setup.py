from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='TESTE',
    version='0.0.1',
    url='https://github.com/ElisabeteOlimpio/TESTE.git',
    license='MIT License',
    author='Elisabete Olimpio',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='olimpioelisabete@gmail.com',
    keywords='Pacote',
    description='Exemplo de pacote PyPI',
    packages=['TESTE'],
    install_requires=['numpy'])
