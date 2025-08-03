from setuptools import setup, find_packages

setup(
    name='django_dev_toolkit',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
    ],
    description='Package for Django development utilities',
    author='anirudh_mk',
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
)