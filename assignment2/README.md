# |_Sree Poojitha Paruchuri`s stats_in_python.py assignment._|
# Assignment Description
This python program calculates the descriptive statistics for a given data set. It calculates the count, average, mean, median,
maximum, minimum, variance and standard deviation of a specific column in the data file.

# Usage
usage_examples = [
    f"To run the program, use the following command in the terminal:",
    f"```\npython stats_in_python.py <file_name> <column_to_parse>\n```",
    <file_name>`: The name of the text file that contains the dataset.",
    `<column_to_parse>`: The index of the column (0-based) in the dataset from which you want to calculate statistics.",
    f"Example:",
    f"```shell",
    f"python stats_in_python.py data.txt 1",
    f"```",
]

# Program Overview
program_components = [
    "The program consists of the following components:",
    "- **Argument Parsing**: The program parses command-line arguments to get the file name and the column to parse. It handles exceptions for missing arguments and invalid column values.",
    "- **Data Parsing**: It reads the specified file line by line and attempts to extract valid numbers from the specified column. Any lines with invalid or non-numeric data are skipped, and the program provides error messages.",
    "- **Statistics Calculation**: After parsing the data, the program calculates the count, average, maximum, minimum, variance, standard deviation, and median of the valid numbers.",
]

# Expected Output
(
    "The program will provide the following statistics as output:\n"

    "- **Column**: The index of the column being analyzed.\n"
    "- **Count**: The total number of lines in the dataset.\n"
    "- **ValidNum**: The count of valid numbers in the specified column.\n"
    "- **Average**: The mean of the valid numbers.\n"
    "- **Maximum**: The maximum value in the column.\n"
    "- **Minimum**: The minimum value in the column.\n"
    "- **Variance**: The variance of the valid numbers.\n"
    "- **Std Dev**: The standard deviation of the valid numbers.\n"
    "- **Median**: The median value of the valid numbers."
)

# Important Functions
[
    "The program is organized into a `main` function where the majority of the code is executed. The key components and functions within the program are as follows:",

    "1. **main()**: The main function that parses command-line arguments, reads the data file, and calculates statistics. It also handles exceptions and error messages.",
    "2. **Data Parsing**: The program extracts and processes data from the input file, skipping invalid data and recording valid numbers in the `numbers` list.",
    "3. **Statistics Calculation**: The program calculates various statistics, including count, average, maximum, minimum, variance, standard deviation, and median. These values are then printed to the console.",
]



