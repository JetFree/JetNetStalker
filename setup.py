from distutils.core import setup

setup(
    name="JetNetStalker",
    version="1.0",
    description="Allow to download data from https://www.imgur.com",
    author="Jet Free",
    author_email="l7egnf@gmail.com",
    packages=["scripts"],
    package_dir={'scripts': 'scripts'},
    package_data={'scripts': ['*.dat']},
)
