import parser
import sys
from pathlib import Path

import numpy as np

from calculator import Calculator


def count_error(data: list[float], *, check_gross_errors: bool = False) -> tuple[float, float]:
    """Count average and squared error for given data.

    Args:
    ----
        data (list[float, ...]): data to count average and squared error.
        check_gross_errors (bool, optional): whether to check for rude values. Defaults to False.

    Returns:
    -------
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
    ----
        data (list[float, ...]): data to delete rude values from.
        squared_error (float): squared error.
        average (float): average error.

    Returns:
    -------
        tuple[list[float, ...], bool]: data without rude values and whether rude values were found.
    """
    found_gross_error = False

    for i in data:
        # TODO(TheCrabilia): extract 2.29 to constant. What the name should be?
        if abs(i - average) / squared_error > 2.29:
            data.remove(i)
            found_gross_error = True
    return data, found_gross_error


def get_input_data(file: Path) -> list[float]:
    """Get data and author from input file.

    Input file should be in the following format:
    <author>
    <data1 data2 ...>

    Returns
    -------
        list[float]: data from input file.

    """
    return [float(i) for i in file.read_text().strip().split(" ")]


def handle_file_output(file: Path, data: str) -> None:
    """Handle file output.

    Args:
    ----
        file (Path): file to write data to.
        data (str): data to write to file.
    """
    if file.exists():
        print(f"{file} already exists. Overwrite? [y/n]", end=" ")
        if input() not in "yY":
            return

    with file.open("w") as file:
        file.write(data)


def main() -> None:  # noqa: D103
    data = get_input_data(args.filename)
    average, squared_error = count_error(data)
    absolute_error = squared_error * 2.57
    relative_error = absolute_error / average * 100  # noqa: F841


if __name__ == "__main__":
    config = parser.parse()
    calc = Calculator.from_config(config)

    data = get_input_data(config.filename)
    document = calc.calculate(data).render()

    if config.output == Path("."):
        sys.stdout.write(document)
    else:
        handle_file_output(config.output, document)
