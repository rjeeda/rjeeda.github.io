import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='pkg_name',
    version='0.0.1',
    author='Joeyta Banerjee',
    author_email='jbanerje@caltech.edu',
    description='Microtubule catastrophe analysis',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    install_requires=["numpy","pandas","bebi103","bokeh>=1.4.0"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
