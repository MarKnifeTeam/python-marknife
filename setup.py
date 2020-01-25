import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="marknife",
    version="0.0.1",
    author="Jose Bernalte",
    author_email="hello@josebernalte.com",
    description="Marknife API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarKnifeTeam/python-marknife",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests>=2.22.0'],
)
