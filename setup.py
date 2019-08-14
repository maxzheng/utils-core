import setuptools


setuptools.setup(
    name='utils-core',
    version='0.1.0',

    author='Max Zheng',
    author_email='maxzheng.os@gmail.com',

    description='General utilities on top of Python standard libraries',
    long_description=open('README.rst').read(),

    url='https://github.com/maxzheng/utils-core',

    install_requires=open('requirements.txt').read(),

    license='MIT',

    packages=setuptools.find_packages(),
    include_package_data=True,

    python_requires='>=3.6',
    setup_requires=['setuptools-git', 'wheel'],

    # entry_points={
    #    'console_scripts': [
    #        'script_name = package.module:entry_callable',
    #    ],
    # },

    classifiers=[
      'Development Status :: 5 - Production/Stable',

      'Intended Audience :: Developers',
      'Topic :: Software Development :: Libraries :: Python Modules',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],

    keywords='general utilities for standard library',
)
