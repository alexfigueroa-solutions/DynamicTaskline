from setuptools import setup, find_packages

setup(
    name='dynamic-taskline',
    version='0.1.0',
    description='A dynamic task management tool',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    url='URL to your project\'s home page',  # Replace with your URL
    packages=find_packages(),
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        # List your dependencies here
        # e.g., 'requests>=2.25.1',
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.1',
            'black>=20.8b1',
            # Other development dependencies
        ],
        'test': [
            'pytest>=6.2.1',
            # Other test dependencies
        ],
    },
    entry_points={
        'console_scripts': [
            'dtl=run:main',
        ],
    },
    include_package_data=True,
)
