import os
import sys
from datetime import datetime

def write_to_file(matching_lines, timecode, substring, part_number):
    """Write matching lines to a file in the specified format."""
    output_filename = f"{timecode}_{substring}_part{part_number}.txt"
    with open(output_filename, 'w', encoding='utf-8') as output:
        # Write in requested format: [line1,line2,...]
        output.write('[' + ','.join(f'"{line}"' for line in matching_lines) + ']')
    print(f"Created file: {output_filename} with {len(matching_lines)} lines")

def process_file(input_file, substring, max_lines_per_file=20000):
    # Get current time for filename
    timecode = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Lists to store matching lines
    matching_lines = []

    # Counter for total lines processed and matches found
    total_lines = 0
    matches_found = 0
    part_number = 1

    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                total_lines += 1
                # Check if substring exists in line
                if substring.lower() in line.lower():
                    # Remove whitespace and add to list
                    matching_lines.append(line.strip())
                    matches_found += 1

                    # Write to file if we reach max_lines_per_file
                    if len(matching_lines) >= max_lines_per_file:
                        write_to_file(matching_lines, timecode, substring, part_number)
                        matching_lines = []  # Reset the list
                        part_number += 1

                # Print progress
                # print(f"Processed {total_lines} lines, found {matches_found} matches")

        # Write any remaining lines to a final file
        if matching_lines:
            write_to_file(matching_lines, timecode, substring, part_number)

        # Print summary
        if matches_found > 0:
            print(f"\nTotal files created: {part_number}")
            print(f"Total lines processed: {total_lines}")
            print(f"Total matches found: {matches_found}")
        else:
            print(f"\nNo matches found for substring '{substring}'")
            print(f"Total lines processed: {total_lines}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "data.txt"
    # Default substring is .jpg
    substring = ".jpg"

    # Check for command-line argument
    if len(sys.argv) > 1:
        substring = sys.argv[1]

    process_file(input_file, substring)
