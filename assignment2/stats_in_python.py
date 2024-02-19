"""
Sree Poojitha Paruchuri
File : stats_in_python.py
"""
import math
import sys

def main():
    """"Main function is used to trigger the program"""
    try:
        file_name = sys.argv[1]
        column_to_parse = int(sys.argv[2])
    except IndexError:
        print("Usage: python stats_in_python.py <file_name> <column_to_parse>")
        sys.exit(1)
    except ValueError:
        print("Error: Column argument should be an integer.")
        sys.exit(1)


    #List to store all number values and valid_numbers
    numbers = []
    count = 0

    with open(file_name, 'r') as infile:
        for line in infile:
            count = count + 1
            rows = line.split("\t")
            # Check for valid numbers.
            try:
                if not math.isnan(float(rows[column_to_parse])):
                    numbers.append(float(rows[column_to_parse]))
            except ValueError as error:
                error_message = str(error)
                print(f"Skipping line number {count}: {error_message}")
            except IndexError:
                print(f"Exiting: There is no valid 'list index' in column {column_to_parse} "
                      f"in line {count} in file: {file_name}")
                sys.exit()

    if len(numbers) == 0:
        print(f"Error: There were no valid number(s) in column "
              f"{column_to_parse} in file: {file_name}")
        sys.exit()

        # Print Statistics.
    print("    Column   = ", column_to_parse)
    print("\n")
    print(f"        Count    = {count:.3f}")
    print(f"        ValidNum = {len(numbers):.3f}")

    # Calculate mean of numbers.
    total = 0
    for number in numbers:
        total += number
    mean = total / len(numbers)
    print(f"        Average  = {mean:.3f}")
    #printing maximum and minimum values
    print(f"        Maximum  = {max(numbers):.3f}")
    print(f"        Minimum  = {min(numbers):.3f}")

    # Calculate variance of numbers.
    variance = 0
    if len(numbers) > 1:
        for number in numbers:
            variance += math.pow((number - mean), 2)
        variance = variance / (len(numbers) - 1)
    print(f"        Variance = {variance:.3f}")

    # Calculate standard deviation of numbers.
    standard_deviation = math.pow(variance, 0.5)
    print(f"        Std Dev  = {standard_deviation:.3f}")

    # Calculate median of numbers.
    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        median = (numbers[mid] + numbers[mid - 1]) / 2
    else:
        median = numbers[mid]
    print(f"        Median   = {median:.3f}")


if __name__ == "__main__":
    main()
