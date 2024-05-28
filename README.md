<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

-   [Lion's example Python package](#lions-example-python-package)
    -   [Description](#description)
        -   [Dependencies](#dependencies)
        -   [Install](#install)
        -   [Develope](#develope)
            -   [Generate distribution archives for the package.](#generate-distribution-archives-for-the-package)
            -   [Build wheel](#build-wheel)
            -   [Run pre-commit](#run-pre-commit)
            -   [Document](#document)
    -   [Help](#help)
    -   [Authors](#authors)
    -   [Version History](#version-history)
    -   [License](#license)
    -   [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Example Python Package

This repository provides an example of a modern Python package. It demonstrates best
practices for structuring, documenting, and distributing Python packages.

## Project Structure

Firstly, this project adopts the
[src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout),
which offers
[several advantages over the traditional flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).

Secondly, This project has a
[namespace package](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages)
called `zionnamespacepackage` and three packages, `firstpackage`, `secondpackage`, and
`effectivepython`.

## Using the Package

This section guides you through the setup and use of this package.

### Setup the Virtual Environment

We need to
[always use a virtual environment](https://realpython.com/python-virtual-environments-a-primer/).
While `pip` alone is sufficient to install from pre-built binary archives, up-to-date
copies of the `setuptools` and `wheel` projects are useful to ensure us can also install
from source archives. Actually, updating `pip` `setuptools` and `wheel` may not be
necessary because a modern python package defines all prerequites in the section of
`[build-system]` of `pyproject.toml`.

```shell
python3.10 -m venv venv_template_project \
&& source venv_template_project/bin/activate \
&& python3 -m pip install --upgrade pip setuptools wheel
```

### Installing the Package

#### Install from GitHub Directly

To install directly from a specific branch on GitHub:

```
python3 -m pip install git+ssh://github.com/lionlai1989/python_example_package.git@<branch_name>
```

<branch_name>: Specify the branch from which to install. `pip` will handle the
downloading and building of the package.

#### Install from the Python Package Index (PyPI)

_This method is currently not supported._

If the package is available on PyPI, you can install it using:

```shell
python3 -m pip install python_example_package
```

#### Install from wheel

_This method is currently not supported._

#### Git Clone and Install from Source

While cloning the repository and installing from source is possible, it generally
defeats the purpose of creating a distributable Python package. _This method is
typically **not recommended** unless necessary for development to the package itself_:

```shell
git clone git@github.com/lionlai1989/python_example_package.git \
&& cd template-python-package \
&& python3 -m pip install .
```

## Developing the Package

This section outlines the steps for developing the template package.

### Setup the Virtual Environment

Again, set up a virtual environment to isolate package dependencies.

```shell
git clone git@github.com:lionlai1989/my_example_python_package.git --recursive \
&& python3.10 -m venv venv_template_project \
&& source venv_template_project/bin/activate \
&& python3 -m pip install --upgrade pip setuptools wheel
```

### Setup the Development Environment

This includes installing the project in
[editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)
along with optional dependencies for development and testing as specified in
`pyproject.toml`.

```shell
python3 -m pip install -e '.[dev,test]'
```

Use `CMAKE_RUNTIME_OUTPUT_DIRECTORY` in setup.py to make executable show up in the path.
This code can only work in normal mode, but not in editable mode.

## Generate distribution archives for the package.

Read https://packaging.python.org/en/latest/tutorials/packaging-projects/ python3 -m pip
install --upgrade build python3 -m build This command should output a lot of text and
once completed should generate two files in the dist directory:

```shell
dist/
  example-package-YOUR-USERNAME-HERE-0.0.1-py3-none-any.whl
  example-package-YOUR-USERNAME-HERE-0.0.1.tar.gz
```

### Build wheel

To build a wheel, run the following command:

```
python3 -m pip install --upgrade wheel
python3 setup.py sdist bdist_wheel
```

## Testing the Package

The `tests/` directory mirrors the structure in `src/`. We use `pytest` along with
coverage reporting for our tests:

```shell
pytest tests --cov=.
```

If the setup and code are correct, you should see an output similar to:

```text
================================================= 25 passed in 0.24s ==================================================
```

## Linting and Formatting

For linting and formatting, we use ruff. This tool helps ensure that our codebase
maintains a consistent style.

```shell
ruff check --fix
ruff format
```

Ideally, it would be nicer to include linting in CI.

## Working in VS Code

-   install `ruff` extension.
-   use `rewrap` extension. do not change the default line length of this extension.

## Run pre-commit

Run `pre-commit run --all-files` in architect_blueprint. Install
`sudo apt install shellcheck`

## Building a Docker Image from Dockerfile

Building a Docker image can help us to test this Python template package in a consistent
environment.

```
docker build -t python-template -f Dockerfile .
```

Once the Docker image is built, we can run it as a container to execute all tests
located in the `tests/` directory using `pytest` with the following command:

```
docker run --rm python-template
```

The expected output should indicate all tests passing as follows:

```
============================== 25 passed in 0.13s ==============================
```

## GitHub CI (and CD?)

Continuous Integration (CI) serves as the gatekeeper for this repository. It
automatically running tests on every push and pull request.

We would recommend addressing any failures in the CI process before proceeding with your
changes.

Note that Homee AI does not use GitHub Enterprise; therefore, pull requests will not be
automatically blocked if CI fails.

This package is primarily designed as a Python library, which makes Continuous
Deployment (CD) less relevant. However, if you have ideas for CD in this context, please
initiate a discussion. Your contributions are welcome!

## Building and Publishing the Package

To be dicussed.

References: Source distribution format:
https://packaging.python.org/en/latest/specifications/source-distribution-format/#source-distribution-format

Binary distribution format:
https://packaging.python.org/en/latest/specifications/binary-distribution-format/

https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
https://realpython.com/pypi-publish-python-package/

## Document

The table of contents of this file can be regenerated with the following steps.

-   Create a `temp` folder and copy/paste this `README.md` file into `temp`.
-   `cd` to `temp` and run `docker run --rm -it -v $(pwd):/usr/src jorgeandrada/doctoc`
-   Copy/paste `README.md` to the original location and delete `temp`.

## Help

Any feedback, comments, and questions about this project are welcome, as are any
contributions you'd like to make. Please feel free to create an issue or a pull request.
Let's improve this template and make life easier for Python programmers.

## Authors

[@lionlai](https://github.com/lionlai1989)

## Version History

-   0.0.1
    -   Various bug fixes and optimizations
-   0.0.0
    -   Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for
details

## Acknowledgments

Explore the inspiration and references listed here to further expand your knowledge and
sharpen your skills.

1. Learn more about the structure of a project

-   https://stackoverflow.com/questions/62983756/what-is-pyproject-toml-file-for
-   https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
-   https://docs.pytest.org/en/6.2.x/goodpractices.html
-   https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/

2. Customize installation with `cmake` and `setuptools`:

-   https://blog.caref.xyz/computer%20tech/python-setup/
-   https://www.programcreek.com/python/example/88191/setuptools.command.develop.develop
-   https://setuptools.pypa.io/en/latest/userguide/extension.html
-   https://stackoverflow.com/questions/33168482/compiling-installing-c-executable-using-pythons-setuptools-setup-py
-   https://stackoverflow.com/questions/64286409/how-to-extend-a-python-package-by-binary-executables
-   https://imhuwq.com/tags/c/
-   https://martinopilia.com/posts/2018/09/15/building-python-extension.html
-   https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py
-   https://setuptools.pypa.io/en/latest/userguide/ext_modules.html
-   https://stackoverflow.com/questions/47360113/compile-c-library-on-pip-install
-   https://www.activestate.com/blog/how-to-build-and-install-c-libraries-in-python/
-   https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py
-   https://stackoverflow.com/questions/50082055/python-setuptools-first-build-from-sources-then-install
-   https://github.com/gemtools/gemtools
-   https://zhuanlan.zhihu.com/p/276461821
-   https://stackoverflow.com/questions/68472281/how-to-compile-c-c-when-installing-a-python-package
-   https://github.com/PacktPublishing/CMake-Cookbook/tree/305c6981cbbcb270eb225f69a7a0e25084cee484/chapter-11
