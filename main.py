import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Any, Union

import numpy as np
import scipy

from renderer import Renderer

INPUT_FILE = "input.txt"


def count_error(data: list[float], *, check_gross_errors: bool = False) -> tuple[float, float]:
    """Count average and squared error for given data.

    Args:
        data (list[float, ...]): data to count average and squared error.
        check_gross_errors (bool, optional): whether to check for rude values. Defaults to False.

    Returns:
        tuple[float, float]: average and squared error.
    """
    # Finding the average
    average = np.average(data)

    # Finding the squared error
    squared_error = 0
    for i in data:
        squared_error += (i - average) ** 2
    squared_error = (squared_error / (len(data) * (len(data) - 1))) ** 0.5

    if not check_gross_errors:
        data, found_gross_error = delete_gross_errors(data, squared_error, average)
        if found_gross_error:
            average, squared_error = count_error(data, check_gross_errors=True)
            return average, squared_error

    return average, squared_error


def delete_gross_errors(data: list[float], squared_error: float, average: float) -> tuple[list[float], bool]:
    """Delete gross errors from data.

    Args:
        data (list[float, ...]): data to delete rude values from.
        squared_error (float): squared error.
        average (float): average error.

    Returns:
        tuple[list[float, ...], bool]: data without rude values and whether rude values were found.
    """
    found_gross_error = False

    for i in data:
        # TODO(TheCrabilia): extract 2.29 to constant. What the name should be?
        if abs(i - average) / squared_error > 2.29:
            data.remove(i)
            found_gross_error = True
    return data, found_gross_error


def format_template(**values: dict[str, Any]) -> str:
    """Format template with given values.

    Args:
        **values: values to format template with.

    Returns:
        str: formatted template.
    """
    renderer = Renderer()
    return renderer.render("template.md", values)


def get_student_coef(count: Union[int, np.Inf], probability: float = 0.95) -> float:
    """Get student coefficient for specified measurement count and confidence probability.

    Args:
        count (int | numpy.Inf): measurement count.
        probability (float): confidence probability.

    Returns:
        float: student coefficient.
    """
    return scipy.stats.t.ppf((1 + probability) / 2, count - 1)


def get_input_data(file: Path) -> list[float]:
    """Get data and author from input file.

    Input file should be in the following format:
    <author>
    <data1 data2 ...>

    Returns:
        list[float]: data from input file.

    """
    with file.open("r", encoding="latin-1") as file:
        data = file.readlines()
        return [float(i) for i in data[1].split(",")]


def handle_file_output(file: Path, data: str) -> None:
    if file.exists():
        print(f"{file} already exists. Overwrite? [y/n]", end=" ")
        if input() not in "yY":
            return

    with file.open("w", encoding="latin-1") as file:
        file.write(data)


def parse_arguments() -> Namespace:
    """Parses CLI arguments.

    Returns:
        Namespace: parsed arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file that contains data to process", type=Path)
    parser.add_argument("-o", "--output", help="output file name", type=Path)
    parser.add_argument("-a", "--author", help="author name", type=str)

    return parser.parse_args()


def main() -> None:  # noqa: D103
    data = get_input_data(args.filename)
    average, squared_error = count_error(data)
    absolute_error = squared_error * 2.57
    relative_error = absolute_error / average * 100

    result = format_template(
        author=args.author,
        average=f"{average:.2f}",
        squared_error=f"{squared_error:.3f}",
        absolute_error=f"{absolute_error:.2f}",
        relative_error=f"{relative_error:.2f}",
        length=len(data),
        value=r"\gamma",
    )

    if args.output is None:
        sys.stdout.write(result)
    else:
        handle_file_output(args.output, result)


if __name__ == "__main__":
    args = parse_arguments()
    main()
