from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

def readme_type():
    return "text/x-rst"

setup(
    name='iris',
    version = '1.0.6',

    description='A Python project for Illumon Iris',

    long_description=readme(),
    long_description_content_type=readme_type(),

    url='https://deephaven.io/',
    author='Deephaven Data Labs LLC',
    author_email='python@deephaven.io',

    license='Apache 2.0',

    keywords='Illumon Iris Deephaven',
    packages=['iris'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
