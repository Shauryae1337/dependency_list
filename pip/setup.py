from setuptools import setup, find_packages
import os
from pathlib import Path

# Read the contents of README.md
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()

# Get version from version.py
def get_version():
    version_file = Path(__file__).parent / "version.py"
    if version_file.exists():
        with open(version_file) as f:
            locals_dict = {}
            exec(f.read(), globals(), locals_dict)
            return locals_dict.get("__version__", "0.0.0")
    return "0.0.0"

# Get requirements from requirements.txt
def get_requirements():
    requirements_file = Path(__file__).parent / "requirements.txt"
    if requirements_file.exists():
        with open(requirements_file) as f:
            return f.read().splitlines()
    return []

setup(
    name="your-project-name",
    version=get_version(),
    description="A brief description of your project",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://your-project-url.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=get_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.1.2",
            "flake8>=6.0.0",
            "black>=23.3.0",
            "isort>=5.12.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-autodoc-typehints>=1.19.0",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": [
            "your_command=your_package.main:main",
        ],
    },
    project_urls={
        "Documentation": "https://your-project-url.com/docs",
        "Source Code": "https://your-project-url.com/source",
        "Issue Tracker": "https://your-project-url.com/issues",
    },
)
