from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_svimg",
    version="0.0.1",
    author="Sandro Vieira",
    author_email="sandro-vieira@outlook.com.br",
    description="Making it easy to create image processing packages in Python using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sandro-vieira/dio-project-procimgpython",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)