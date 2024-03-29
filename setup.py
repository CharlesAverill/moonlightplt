import setuptools

version = "0.2.2"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='moonlightplt',
    version=version,
    author="Charles Averill",
    author_email="charlesaverill20@gmail.com",
    description="Matplotlib wave plotting and animation made easy",
    long_description=long_description,
    install_requires=["matplotlib", "numpy", "scipy"],
    long_description_content_type="text/markdown",
    url="https://github.com/CharlesAverill/moonlightplt/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Matplotlib"
    ]
)
