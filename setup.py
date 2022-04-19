import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MostPopularNews-Indonesia",
    version="0.1",
    author="Aditiya Ahmad",
    author_email="aditiyahmd@gmail.com",
    description="this project will get most popular news from detik.com (indonesian news portal)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kenzo-aaf/most-popular-news",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    #package_dir={"": "src"},
    #packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
