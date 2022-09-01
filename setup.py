from setuptools import setup, find_packages

setup(
    name='syt',
    version='1.0',
    description='Simple YACS Templating extension',
    author='Chris Boyle',
    author_email='chris@cmjb.tech',
    packages=find_packages(),
    install_requires=['wheel'],
    requires=['yacs'],
    extras_require=dict(
        test='pytest'
    )
)
