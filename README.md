# Physics Labs Automation Script

It is a Python script designed to automate certain calculations for physics lab data. It includes a function called `count_error` that performs error calculations on a given dataset. This documentation provides a detailed explanation of the script's purpose, function, and usage.

## Purpose

Physics labs often involve collecting data and analyzing it to determine experimental results. One important aspect of data analysis is the calculation of errors, which helps assess the accuracy and reliability of the measurements. This script simplifies the process of error calculations by providing a function that performs the necessary computations.

## Usage

1. Install required libraries `pip install -r requirements.txt`
2. Run the script `python main.py`

## Functions

`count_error(data: list[float]) -> None`

1. **Average Calculation**: The function calculates the average (mean) of the dataset.
2. **Squared Error Calculation**: It calculates the squared error for each data point by subtracting the average from each value, squaring the difference, and summing the squared errors.
3. **Standard Deviation Calculation**: The squared error is then divided by (len(data) * (len(data) - 1)) and the square root of the result is taken. This yields the standard deviation (squared error) of the dataset.
4. **Identification of Rude Values**: The function checks if any data point in the dataset exceeds a certain threshold value (2.29 in this case). If a value is deemed "rude" based on this threshold, it is removed from the dataset.
5. **Recalculating Average and Squared Error**: After removing any rude values, the function recalculates the average and squared error of the modified dataset.
5. **Error Measures**: The function calculates two additional error measures:
    * Absolute Error: The squared error is multiplied by 2.57 to obtain the absolute error.
    * Relative Error: The absolute error is divided by the average to obtain the relative error.
6. **Output**: The function prints the calculated average, squared error, modified dataset (after removing rude values), and the calculated absolute and relative errors.
