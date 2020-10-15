from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/opunsoars/titanic_datascience',
    author='Vinay Warrier', 
    author_email='vinay.warrier@gmail.com',
    license='MIT',
    packages=['titanic'],
    install_requires=[
	'pypandoc>=1.4'
    ]
)
