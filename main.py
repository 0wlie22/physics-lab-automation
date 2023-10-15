from pathlib import Path
from typing import Any

import numpy as np
import scipy
import math

TEMPLATE_FILE = "template.md"
INPUT_FILE = "input.txt"
RESULT_FILE = "result.md"
START_LENGTH = 0
END_LENGTH = 0


def count_error(
    data: list[float], *, check_gross_errors: bool = False
) -> tuple[float, float]:
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


def delete_gross_errors(
    data: list[float], squared_error: float, average: float
) -> tuple[list[float], bool]:
    """Delete gross errors from data.

    Args:
        data (list[float, ...]): data to delete rude values from.
        squared_error (float): squared error.
        average (float): average error.

    Returns:
        tuple[list[float, ...], bool]: data without rude values and whether rude values were found.
    """
    found_gross_error = False

    counter = 0

    for i in data:
        counter += 1
        value = abs(i - average) / squared_error
        if value > 2.6:
            data.remove(i)
            found_gross_error = True
            print(f"Found gross error: {i}, index: {counter}")
    return data, found_gross_error


def format_template(**values: dict[str, Any]) -> str:
    """Format template with given values.

    Args:
        **values: values to format template with.

    Returns:
        str: formatted template.
    """
    formatted_template = f"<div align=right>{get_author()}</div>\n"

    with Path.open(TEMPLATE_FILE, "r", encoding="latin-1") as file:
        symbol = file.read(1)

        while symbol:
            if symbol == "<":
                next_symbol = file.read(1)

                if next_symbol == "<":
                    formatted_template += "<"
                else:
                    key = ""
                    while next_symbol != ">":
                        key += next_symbol
                        next_symbol = file.read(1)

                    formatted_template += str(values.get(key))
            else:
                formatted_template += symbol

            symbol = file.read(1)

    return formatted_template


def get_student_coef(count: int or np.inf, probability: float = 0.95) -> float:
    """Get student coefficient for specified measurement count and confidence probability.

    Args:
        count (int | numpy.inf): measurement count.
        probability (float): confidence probability.

    Returns:
        float: student coefficient.
    """
    return scipy.stats.t.ppf((1 + probability) / 2, count - 1)


def get_input_data() -> list[float]:
    """Get data and author from input file.

    Input file should be in the following format:
    <author>
    <data1, data2, ...>

    Returns
        list[str]
    """
    with Path.open(INPUT_FILE, "r", encoding="latin-1") as file:
        data = file.readlines()
        return [float(i) for i in data[1].split(",")]


def get_author() -> str:
    """Get author from input file.

    Input file should be in the following format:
    <author>
    <data1, data2, ...>.

    Returns
        str

    """
    with Path.open(INPUT_FILE, "r", encoding="latin-1") as file:
        data = file.readlines()
        return data[0][:-1]


def count_values(data: list[float]) -> list[float]:
    start_value = 0
    new_data = []
    for i in range(len(data)):
        value = data[i]/(np.cos(math.radians(start_value)))**2
        new_data.append(value)
        print(start_value, value, np.cos(math.radians(start_value)))
        start_value += 5

    return new_data

def main() -> None:  # noqa: D103
    data = count_values(get_input_data())
    average, squared_error = count_error(data)
    absolute_error = squared_error * 2.57
    relative_error = absolute_error / average * 100

    result = (
        format_template(
            average=f"{average:.2f}",
            squared_error=f"{squared_error:.3f}",
            absolute_error=f"{absolute_error:.2f}",
            relative_error=f"{relative_error:.2f}",
            length=START_LENGTH,
            value="I",
        ),
    )

    with Path.open(RESULT_FILE, "w", encoding="latin-1") as file:
        for line in result:
            file.write(line)


if __name__ == "__main__":
    main()
