from setuptools import setup, find_packages

setup(
    name='custom-binary-encoder',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
    ],
    test_suite='tests',
    author='Alexey Kozhakin',
    author_email='alexeykozhakin@gmail.com',
    description='A custom binary encoder for categorical features in machine learning.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AlexeyKozhakin/custom-binary-encoder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
