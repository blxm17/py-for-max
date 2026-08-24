import csv
import sys


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "csv":
        load_and_display_csv(sys.argv[2])
    else:
        print("Command line arguments:")
        for i, arg in enumerate(sys.argv[1:]):
            print(f"Argument {i + 1}: {arg}")  # Adjusted to start from index 1


def load_and_display_csv(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"CSV Row {reader.line_num}: {row}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


if __name__ == "__main__":
    main()
