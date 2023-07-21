"""A command line entry point file."""

import argparse
import time
from pathlib import Path

# from typing import Any, Callable, Iterable, List, Optional, Sequence, Tuple, Type, Union
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple

from loguru import logger


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
