# dio-project-procimgpython
Making it easy to create image processing packages in Python

# package_name

**Description** 
The package package_name is used to:
	Processing:
		- Histogram matching 
		- Structural similarity
		- Resize image
	Utils:
		- Read image
		- Save image
		- Plot image
		- Plot result
		- Plot histogram

**How the package should be built**
Would you like to know more, [click here](https://setuptools.pypa.io/en/latest/setuptools.html).

```pip
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools

python setup.py sdist bdist_wheel
```

**Publishing on Test Pypi**

```Test Pypi
python -m twine upload --repository-utl http://test.pypi.org/legacy/dist/*
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install image_processing_svimg

```bash
pip install image_processing_svimg
```

## Usage

```Python code
from image_processing_svimg.utils import io, plot
from image_processing_svimg.processing import combination, transformation
```

## Author
Sandro Vieira

## License
[MIT](https://choosealicense.com/licenses/mit/)