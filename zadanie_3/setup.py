from setuptools import setup, find_packages

setup(
    name='zadanie_3_lib',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Mateusz Gruszczynski',
    author_email='grucha2000@o2.pl',
    description='Biblioteka do przetwarzania danych, operacji matematycznych i manipulacji tekstem.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MateusZST2025/-python-intro',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
