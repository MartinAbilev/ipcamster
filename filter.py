import os
from datetime import datetime

def process_file(input_file, substring):
    # Get current time for filename
    timecode = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Prepare output filename
    output_filename = f"{timecode}_{substring}.txt"

    # Lists to store matching lines
    matching_lines = []

    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                # Check if substring exists in line
                if substring.lower() in line.lower():
                    # Remove whitespace and add to list
                    matching_lines.append(line.strip())

        # Write to output file if matches found
        if matching_lines:
            with open(output_filename, 'w', encoding='utf-8') as output:
                # Write in requested format: [line1,line2,...]
                output.write('[' + ','.join(f'"{line}"' for line in matching_lines) + ']')
            print(f"Created file: {output_filename}")
        else:
            print(f"No matches found for substring '{substring}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "data.txt"
    substring = ".pdf"
    process_file(input_file, substring)
