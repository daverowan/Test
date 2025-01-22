import sys
import csv

def compute_stats(values):
    """ Computes basic statistics (minimum, maximum, average, and median) for a list of numerical values."""

    numeric_values = [x for x in values if isinstance(x, (int, float))]
    if not numeric_values:
        return None, None, None, None

    values.sort()
    o_min = min(values)
    o_max = max(values)
    o_avg = sum(values) / len(values)
    midpoint = len(values) // 2
    o_median = values[midpoint] if len(values) % 2 != 0 else (values[midpoint - 1] + values[midpoint]) / 2
    return o_min, o_max, o_avg, o_median

def main():
    """Main function to process data from a file, extract a specified column or entire file,
    and compute statistical metrics (minimum, maximum, average, and median)."""

    # Ensure the correct number of arguments is given
    if len(sys.argv) != 3:
        print("Usage: python compute_stats2.py <filename> <column_number>")
        sys.exit(1)
    filename = None
    column_number = None

    try:
        filename = sys.argv[1]  # Assign the filename to the first argument
        column_number = int(sys.argv[2])  # Column number provided by the user (1-based)
        column_number = column_number - 1  # Convert column number to 0-based index

        # Open the file and process data
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
            # Extract column data as floats while excluding -9999.0
            column_values = [
                float(row[column_number]) for row in reader if float(row[column_number]) != -9999.0
            ]

        # Compute statistics (min, max, average)
        min_value = min(column_values)
        max_value = max(column_values)
        average = sum(column_values) / len(column_values)

        # Print results
        print(f"Minimum: {min_value}")
        print(f"Maximum: {max_value}")
        print(f"Average: {average}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except ValueError:
        print(
            "Error: Invalid column number or non-numeric data. Please provide a valid positive integer and ensure the column contains numeric data.")
        sys.exit(1)
    except IndexError:
        print(f"Error: Column number {column_number} is out of range. Please select a valid column.")
        sys.exit(1)

if __name__ == "__main__":
     main()
     dddff
