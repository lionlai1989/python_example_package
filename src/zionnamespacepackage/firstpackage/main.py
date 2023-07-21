#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""A command line entry point file."""
import os
import argparse
import time
from pathlib import Path
import subprocess
import sys
# from typing import Any, Callable, Iterable, List, Optional, Sequence, Tuple, Type, Union
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple
import importlib

from loguru import logger
import inspect

# add the bin folder to system path

import sysconfig
print(sys.path)
print(sysconfig.get_paths()["purelib"])
module_rootpath = sysconfig.get_paths()["purelib"]

# get the absolute path of venv/lib/python3.8/site-packages
# parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# bin_dir = os.path.join(parent_dir, 'bin')
# os.environ['PATH'] = bin_dir + os.pathsep + os.environ['PATH']

def run_command(cmd, env=os.environ, timeout=None, shell=False):
    """
    Runs a shell command, and print it before running.
    Arguments:
        cmd: list of a command and its arguments, or as a fallback,
            a string to be passed to a shell that will be split into a list.
        env (optional, default value is os.environ): dictionary containing the
            environment variables
        timeout (optional, int): time in seconds after which the function will
            raise an error if the command hasn't returned
        TODO: remove the temporary `shell` argument once all commands use shell=False
        shell (bool): run the command in a subshell. Defaults to False.
    Both stdout and stderr of the shell in which the command is run are those
    of the parent process.
    """
    print("\nRUN: %s" % cmd)
    if not isinstance(cmd, list) and not shell:
        cmd = cmd.split()
    subprocess.run(cmd, shell=shell, stdout=sys.stdout, stderr=sys.stderr,
                   env=env, timeout=timeout, check=True)
    
def typing_showcase(
    fn: Callable[..., Any],
    a_dict: Dict[Any, Any],
    a_tuple: Tuple[Any, ...],
    listoftuple: List[Tuple[Any, ...]],
    numbers: Iterable[int],
    flag: Optional[bool] = None,
) -> None:
    """With regard to type hints, Tuple is not like List.
    Tuple[int] means "a tuple of 1 int"
    Tuple[int, int] means "a tuple of 2 ints"
    List[int] means "a list of ints

    Parameters
    ----------
    numbers : Iterable[int]
        `numbers` type must be sequence if you want to iterate `numbers` and `len(numbers)`.
    flag : Optional[bool], optional
        Read https://stackoverflow.com/questions/51710037/how-should-i-use-the-optional-type-hint
        `Optional[bool] = None` and `Union[bool, None]` are exactly the same thing.
    """
    print(fn, a_tuple, listoftuple, a_dict, numbers, flag)


def BAD_append_to(element, to=[]):
    """This is BAD code. Explain why.
    Read https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
    Python default arguments are evaluated once when the function is defined, not each time the
    function is called (like it is in say, Ruby). This means that if you use a mutable default
    argument and mutate it, you will and have mutated that object for all future calls to the
    function as well."""
    to.append(element)
    return to


def GOOD_append_to(element, to=None):
    """Explain why this GOOD."""
    if to is None:
        to = []
    to.append(element)
    return to


def BAD_create_multipliers():  # This is BAD code. Explain why.
    return [lambda x: i * x for i in range(5)]


def ALSO_BAD_create_multipliers():  # This is BAD code. Explain why.
    multipliers = []
    for i in range(5):

        def multiplier(x):
            return i * x

        multipliers.append(multiplier)

    return multipliers


def GOOD_create_multipliers():
    return [lambda x, i=i: i * x for i in range(5)]


def division_with_error(a: int, b: int):
    try:
        c = a / b
    except Exception as e:
        raise e


def run(args: Optional[List[str]]) -> None:

    typing_showcase(len, {"1": "2"}, (1, 3), [(1, 2), (3, 4)], range(3))

    try:
        division_with_error(a=1, b=0)
    except Exception:
        raise
    # The full stack trackback is returned.
    # Traceback (most recent call last):
    #   File "<stdin>", line 2, in <module>
    #   File "<stdin>", line 5, in f
    #   File "<stdin>", line 3, in f
    # ZeroDivisionError: division by zero


def main() -> None:
    """Entry point of command line."""
    run_command([f"{module_rootpath}/bin/helloworld"])

    logger.add(f"logs/{time.strftime('%Y%m%d_%H%M%S')}.log", retention="10 days")
    logger.info("Starting Pleiades Stereo Processing ...")
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("--gcp-dir", dest="gcp_dir", type=Path, required=True)
    parser.add_argument(
        "--out-efs-dir", type=Path, required=True
    )  # dest is not needed.
    parser.add_argument(
        "--output-resolution",
        type=float,
        nargs=2,
        metavar=("resolution-x-axis", "resolution-y-axis"),
        required=False,
    )
    parser.add_argument(
        "--resample",
        dest="resample",
        action="store_true",
        help="if a model should be resampled",
        required=False,
    )

    run(parser.parse_args())

    logger.info(
        f"\n\nstereo_processing finished in"
        f" {(time.time() - start_time) / 60:.1f} minutes.\n"
    )


if __name__ == "__main__":
    main()
