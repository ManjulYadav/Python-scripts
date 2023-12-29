#!/bin/bash

# Check if the user provided two arguments: input filename and output filename
if [ $# -ne 2 ]; then
  echo "Usage: $0 <input_filename> <output_filename>"
  exit 1
fi

input_filename="$1"
output_filename="$2"

# Check if the input file exists
if [ ! -f "$input_filename" ]; then
  echo "Input file not found: $input_filename"
  exit 1
fi

# Initialize variables
sum=0
sum_squared=0
count=0

# Loop through each line in the input file, remove comments and calculate sum and sum of squares
while read -r line; do
  # Remove comments from the line (lines starting with #)
  line=$(echo "$line" | sed 's/#.*//')
  
  # Use awk to extract the second column value (assuming columns are separated by whitespace)
  value=$(echo "$line" | awk '{print $2}')

  # Check if the value is a valid number
  if [[ "$value" =~ ^[+-]?[0-9]*\.?[0-9]+$ ]]; then
    sum=$(awk "BEGIN {print $sum + $value}")
    sum_squared=$(awk "BEGIN {print $sum_squared + ($value * $value)}")
    count=$((count + 1))
  fi
done < "$input_filename"

# Calculate the average
if [ $count -gt 0 ]; then
  average=$(awk "BEGIN {print $sum / $count}")
  variance=$(awk "BEGIN {print ($sum_squared / $count) - ($average * $average)}")
  std_dev=$(awk "BEGIN {print sqrt($variance)}")
  echo "Average of values in the second column: $average" > "$output_filename"
  echo "Standard Deviation of values in the second column: $std_dev" >> "$output_filename"
else
  echo "No valid values found in the second column." > "$output_filename"
fi

echo "Results written to $output_filename"

