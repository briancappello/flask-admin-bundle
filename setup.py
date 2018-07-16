from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Flask Admin Bundle',
    version='0.2.0',
    description='Integrates Flask Admin with Flask Unchained',
    long_description=long_description,
    url='https://github.com/briancappello/flask-admin-bundle',
    author='Brian Cappello',
    license='MIT',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'flask-admin>=1.5.0',
        'flask-sqlalchemy-bundle>=0.3.1',
        'flask-unchained>=0.3.1',
    ],
    extras_require={
        'dev': [
            'coverage',
            'pytest',
            'pytest-flask',
            'tox',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
