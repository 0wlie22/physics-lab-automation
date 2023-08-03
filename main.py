from pathlib import Path

import numpy as np
import scipy


def count_error(data: list[float, ...], *, check_rude_values: bool = False):
    # Finding the average
    average = np.average(data)

    # Finding the squared error
    squared_error = 0
    for i in data:
        squared_error += (i - average) ** 2
    squared_error = (squared_error / (len(data) * (len(data) - 1))) ** 0.5

    if not check_rude_values:
        data, found_rude_value = delete_rude_values(data, squared_error, average)
        if found_rude_value:
            average, squared_error = count_error(data, check_rude_values=True)
            return average, squared_error

    return average, squared_error


def delete_rude_values(data: list[float, ...], squared_error: float, average: float):
    found_rude_value = False

    for i in data:
        if abs(i - average) / squared_error > 2.29:
            data.remove(i)
            found_rude_value = True
    return data, found_rude_value


def format_template(**kwargs):
    values = kwargs
    formatted_template = "<div align=right>Darja Sedova, 221RDB030</div>"

    with Path.open("template.md") as f:
        symbol = f.read(1)

        while symbol:
            if symbol == "<":
                next_symbol = f.read(1)

                if next_symbol == "<":
                    formatted_template += "<"
                else:
                    key = ""
                    while next_symbol != ">":
                        key += next_symbol
                        next_symbol = f.read(1)

                    formatted_template += str(values.get(key))
            else:
                formatted_template += symbol

            symbol = f.read(1)

    return formatted_template


def get_student_coef(n: int, cp: float = 0.95) -> float:
    """Get student coefficient for specified measurement count and confidence probability.

    Args:
        n (int): measurement count
        cp (float): confidence probability

    Returns:
        float: student coefficient
    """
    return scipy.stats.t.ppf((1 + cp) / 2, n - 1)


def main() -> None:  # noqa: D103
    data = [1.224, 1.333, 1.196, 1.273, 1.220, 1.321, 1.208, 1.212, 1.230, 1.205]
    average, squared_error = count_error(data)
    absolute_error = squared_error * 2.57
    relative_error = absolute_error / average * 100

    print(
        format_template(
            average=f"{average:.2f}",
            squared_error=f"{squared_error:.3f}",
            absolute_error=f"{absolute_error:.2f}",
            relative_error=f"{relative_error:.2f}",
            length=len(data),
            value=r"\gamma",
        ),
    )


if __name__ == "__main__":
    main()
