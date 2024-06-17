# -*- coding: utf-8 -*-
"""setup.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W-kBpRCWSi3G2MHVwE_tGPsJdSb_5nsH
"""

import setuptools

#with open("README.md", "r") as fh:
    #long_description = fh.read()

with open("requirements.txt", 'r') as dependencies:
    requirements = [pkg.strip() for pkg in dependencies]

setuptools.setup(
    name="waternet",
    version="0.0.1",
    author="ICG Innovation",
    author_email="lorenza.nanni@port.ac.uk",
    description="Remote sensing and TinyML for Water Quality",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/lonanni/WaterNets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    install_requires=requirements,
    python_requires='>=3.7',
    exclude = "*.ipynb"
)
