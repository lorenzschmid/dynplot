from distutils.core import setup

setup(
    name='dynplot',
    version='1.0.0',
    author='Lorenz Schmid',
    author_email='lorenzschmid@users.noreply.github.com',
    packages=['dynplot'],
    url='https://github.com/lorenzschmid/dynplot',
    license='LICENSE.txt',
    description='Small matplotlib extension allowing for dynamic plotting.',
    long_description=open('README.rst').read(),
    install_requires=[
        "matplotlib >= 3.0.0"
    ],
)
