from setuptools import setup, find_packages

setup(
    name='devsecops_project',
    version='1.0.0',
    description='A demo project for a CI/CD pipeline using Python, pytest, SonarQube analysis, and Slack notifications.',
    author='Marty Crane',
    author_email='marty.crane.jr@gmail.com',
    url='https://github.com/MrGolbez/devsecops_project',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pytest',
        'pytest-cov'
    ],
    classifiers={
        'Programming Language :: Python :: 3',
    },
    python_requires='>=3.6',
)
