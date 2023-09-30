from pathlib import Path
from typing import Any

import numpy as np
import scipy

TEMPLATE_FILE = "template.md"


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
    # TODO(TheCrabilia): make author configurable
    # https://github.com/0wlie22/physics-lab-automation/issues/5
    formatted_template = "<div align=right>Darja Sedova, 221RDB030</div>\n"

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


def main() -> None:  # noqa: D103
    data = [1.224, 1.333, 1.196, 1.273, 1.220, 1.321, 1.208, 1.212, 1.230, 1.205]
    average, squared_error = count_error(data)
    absolute_error = squared_error * 2.57
    relative_error = absolute_error / average * 100

    result = (
        format_template(
            average=f"{average:.2f}",
            squared_error=f"{squared_error:.3f}",
            absolute_error=f"{absolute_error:.2f}",
            relative_error=f"{relative_error:.2f}",
            length=len(data),
            value=r"\gamma",
        ),
    )

    with Path.open("result.md", "w", encoding="latin-1") as file:
        for line in result:
            file.write(line)


if __name__ == "__main__":
    main()
