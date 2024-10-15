#!/usr/bin/python3

import sys


def parse_log():
    """Function to parse log lines and compute metrics."""
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            # Split the line into parts
            parts = line.split()
            if len(parts) >= 5:
                # Update total file size
                total_size += int(parts[-1])
                code = parts[-2]

                # Update status code counts
                if code in status_codes:
                    status_codes[code] += 1

                # Print metrics every 10 lines
                if line_count % 10 == 0:
                    print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_metrics(total_size, status_codes)


def print_metrics(total_size, status_codes):
    """Print the total size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    parse_log()
