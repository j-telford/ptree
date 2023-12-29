from setuptools import setup, find_packages

# Project metadata
author = "Jay Telford"
email = "hello@jaytelford.me"
version = "0.0.001-alpha"
project_name = "pTREE"
description = "A simple terminal-based file tree generator written in Python using the curses library."
long_description = "README.md"
long_description_content_type = "text/markdown"
source_repo = "https://github.com/j-telford/ptree"
issue_tracker = "https://github.com/j-telford/ptree/issues"

# Development dependencies
dev_dependencies = [
    "pytest",  # Example: Add your development dependencies here
]

# Define the setup
setup(
    name=project_name,
    version=version,
    author=author,
    author_email=email,
    description=description,
    long_description=open(long_description).read(),
    long_description_content_type=long_description_content_type,
    url=source_repo,
    packages=find_packages(),
    install_requires=[
        "curses",
    ],
    extras_require={
        "dev": dev_dependencies,  # Define dev dependencies under the "dev" extras_require key
    },
    python_requires=">=3.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

