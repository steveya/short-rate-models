from setuptools import setup, find_packages

setup(
    name='short-rate-models',
    version='0.1.0',
    author='Steve Yang',
    author_email='steveya@gmail.com',
    description='A package of short rate models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/steveta/short-rate-models',
    packages=find_packages(where='short_rate_models'),
    package_dir={'': 'short_rate_models'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy'
    ],
)