from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cyndaquil',
    version='0.1',    
    description='Python wrapper for the PokéAPI RESTful api',
    url='https://github.com/redjordan1202/PyDex',
    author='Jordan Del Pilar',
    author_email='redjordan123@gmail.com',
    license='MIT',
    packages=['cyndaquil'],
    install_requires=['requests'],
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
)