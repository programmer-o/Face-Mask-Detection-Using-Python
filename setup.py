import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Face Detection app",
    version="0.0.1",
    author="Janak Raikhola",
    author_email="jraikhola@gmail.com",
    description="",
    install_requires='requirements.txt',
    long_description=long_description,
    url="jraikhola.com.np",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)