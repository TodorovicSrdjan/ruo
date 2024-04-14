import csv
import math
import sys


def split_csv(input_file, index, k):
    """Splits a CSV file into k bins and returns the bin at the given index.

    Args:
        input_file: The path to the input CSV file.
        index: The index of the bin to return.
        k: The number of bins to split the CSV file into.

    Returns:
        A list of lists representing the bin of the CSV file at the given index.
    """

    with open(input_file, encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows.pop(0)
    new_rows = []
    new_rows.append(header)

    bin_size = math.ceil(len(rows) / k)

    beginning = bin_size * index
    end = beginning + bin_size if index != k - 1 else None
    new_rows.extend(rows[beginning:end])

    return new_rows


def main():
    # Get the input file, index, and k from the command line.
    input_file = sys.argv[1]
    index = int(sys.argv[2])
    k = int(sys.argv[3])

    # Split the CSV file and print the part at the given index.
    part = split_csv(input_file, index, k)
    
    with open(f'part_{index+1}.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(part)


if __name__ == "__main__":
  main()