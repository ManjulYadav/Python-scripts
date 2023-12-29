#!/bin/bash

# Check if at least three input files are provided
if [ $# -lt 3 ]; then
  echo "Usage: $0 <file1> <file2> <file3> <output_file>"
  exit 1
fi

# Initialize variables
file1="$1"
file2="$2"
file3="$3"
output_file="$4"
concatenated_file="concatenated_data.txt"

# Concatenate the contents of the three input files
cat "$file1" "$file2" "$file3" > "$concatenated_file"

# Calculate the mean and standard deviation
mean=$(awk '{ sum += $1 } END { print sum / NR }' "$concatenated_file")
stddev=$(awk -v mean="$mean" '{ sum += ($1 - mean)^2 } END { print sqrt(sum / NR) }' "$concatenated_file")

# Save the results to the output file
echo "Mean: $mean" > "$output_file"
echo "Standard Deviation: $stddev" >> "$output_file"

echo "Results saved to $output_file"

# Optionally, you can remove the concatenated file
# rm "$concatenated_file"

