import numpy as np

def count_error(data: list[float]) -> None:
    # Finding the average
    average: float = np.average(data)
    print(average)

    # Finding the squared error
    squared_error: float = 0
    for i in data:
        squared_error += (i - average) ** 2
    squared_error = (squared_error/(len(data) * (len(data) - 1)) ) ** 0.5
    print(squared_error)

    # Checking if the data contains a rude value
    koef_data: list[float] = []
    for i in data:
        koef_data.append(abs(i - average) / squared_error)
        if koef_data[-1] > 2.29:
            data.remove(i)
    print(data)

    average: float = np.average(data)
    squared_error: float = 0
    for i in data:
        squared_error += (i - average) ** 2
    squared_error = (squared_error/(len(data) * (len(data) - 1))) ** 0.5

    absolute_error: float = squared_error * 2.57
    relative_error: float = absolute_error / average

    print(f"Average: {average}, Squared error: {squared_error}, Absolute error: {absolute_error}, Relative error: {relative_error}")

def main():
    data: list[float] = [1.224,1.333,1.196,1.273,1.220,1.321,1.208,1.212,1.230,1.205]
    count_error(data)

if __name__ == "__main__":
    main()

