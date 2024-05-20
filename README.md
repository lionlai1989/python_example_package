<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Lion's example Python package](#lions-example-python-package)
  - [Description](#description)
    - [Dependencies](#dependencies)
    - [Install](#install)
    - [Develope](#develope)
      - [Generate distribution archives for the package.](#generate-distribution-archives-for-the-package)
      - [Build wheel](#build-wheel)
      - [Run pre-commit](#run-pre-commit)
      - [Document](#document)
  - [Help](#help)
  - [Authors](#authors)
  - [Version History](#version-history)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Lion's example Python package

Lion's Example Python Package is an open-source Python package designed to help developers gain a fundamental understanding of how Python projects work. It covers various topics, ranging from the basics to advanced concepts, which can save a considerable amount of research time.

## Project Structure
First and foremost, this project adopts the src-layout, which offers several
advantages over the traditional flat layout.

This package covers the following topics:
- Namespace package
- Pre-commit hook
- Automatically build and install a C++ library and executable in the system path.
- Use ruff as the main linter. **(NOTE: It's not done yet.)**

### Dependencies
Theoretically, this package is self-contained, and it downloads all the required software automatically. Therefore, there is no need to install any external dependencies manually. It has been tested on `Python 3.10`.

### Install
- Activate a Python virtual environment and update `pip`:
```
python3 -m venv venv_python_example && source venv_python_example/bin/activate && python3 -m pip install --upgrade pip setuptools wheel
```
- Install from source or:
```
python3 -m pip install "git+ssh://git@github.com/lionlai1989/python_example_package.git"
```

- Clone this repo recursively and install from source:
```
git clone git@github.com:lionlai1989/python_example_package.git --recursive
python3 -m pip install .
```

- Verify installation:  
  After the installation is completed, you can run `examplecmd` to verify the installation.

### Develope
While developing a Python package, we need to install this package in editable
mode.
- Clone this repo recursively, activate a Python virtual environment and update `pip`:
```
git clone git@github.com:lionlai1989/my_example_python_package.git --recursive
python3 -m venv venv_python_example && source venv_python_example/bin/activate && python3 -m pip install --upgrade pip
```
- Install in editable mode:
```
python3 -m pip install -e .
```

Use `CMAKE_RUNTIME_OUTPUT_DIRECTORY` in setup.py to make executable show up in the path.
This code can only work in normal mode, but not in editable mode.

#### Generate distribution archives for the package.
Read https://packaging.python.org/en/latest/tutorials/packaging-projects/
python3 -m pip install --upgrade build
python3 -m build
This command should output a lot of text and once completed should generate two files in the dist directory:
```shell
dist/
  example-package-YOUR-USERNAME-HERE-0.0.1-py3-none-any.whl
  example-package-YOUR-USERNAME-HERE-0.0.1.tar.gz
```
#### Build wheel
To build a wheel, run the following command:
```
python3 -m pip install --upgrade wheel
python3 setup.py sdist bdist_wheel
```

#### Working in VS Code
- install `ruff` extension.
- use `rewrap` extension. do not change the default line length of this extension.

#### Run pre-commit
Run `pre-commit run --all-files` in architect_blueprint.
Install `sudo apt install shellcheck`

#### Document
The table of contents of this file can be regenerated with the following steps.
- Create a `temp` folder and copy/paste this `README.md` file into `temp`.
- `cd` to `temp` and run `docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc`
- Copy/paste `README.md` to the original location and delete `temp`.

## Help

Any feedback, comments, and questions about this project are welcome, as are any contributions you'd like to make. Please feel free to create an issue or a pull request. Let's improve this template and make life easier for Python programmers.


## Authors
[@lionlai](https://github.com/lionlai1989)

## Version History

* 0.0.1
    * Various bug fixes and optimizations
* 0.0.0
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file
for details

## Acknowledgments
Explore the inspiration and references listed here to further expand your knowledge and sharpen your skills.

1. Learn more about the structure of a project
- https://stackoverflow.com/questions/62983756/what-is-pyproject-toml-file-for
- https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
- https://docs.pytest.org/en/6.2.x/goodpractices.html
- https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/

2. Customize installation with `cmake` and `setuptools`:
- https://blog.caref.xyz/computer%20tech/python-setup/
- https://www.programcreek.com/python/example/88191/setuptools.command.develop.develop
- https://setuptools.pypa.io/en/latest/userguide/extension.html
- https://stackoverflow.com/questions/33168482/compiling-installing-c-executable-using-pythons-setuptools-setup-py
- https://stackoverflow.com/questions/64286409/how-to-extend-a-python-package-by-binary-executables
- https://imhuwq.com/tags/c/
- https://martinopilia.com/posts/2018/09/15/building-python-extension.html
- https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py
- https://setuptools.pypa.io/en/latest/userguide/ext_modules.html
- https://stackoverflow.com/questions/47360113/compile-c-library-on-pip-install
- https://www.activestate.com/blog/how-to-build-and-install-c-libraries-in-python/
- https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py
- https://stackoverflow.com/questions/50082055/python-setuptools-first-build-from-sources-then-install
- https://github.com/gemtools/gemtools
- https://zhuanlan.zhihu.com/p/276461821
- https://stackoverflow.com/questions/68472281/how-to-compile-c-c-when-installing-a-python-package
- https://github.com/PacktPublishing/CMake-Cookbook/tree/305c6981cbbcb270eb225f69a7a0e25084cee484/chapter-11
