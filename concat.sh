#!/bin/bash

# ==========================
# Configuration Section
# ==========================

# Hardcoded path to the target directory containing the files to concatenate
TARGET_DIR="./src"

# Hardcoded path to the output file where the concatenated content will be saved
OUTPUT_FILE="./concat.py"  

# ==========================
# Script Execution
# ==========================

# Check if the target directory exists and is a directory
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Target directory '$TARGET_DIR' does not exist or is not a directory."
    exit 1
fi

# Empty the output file if it already exists, or create it
> "$OUTPUT_FILE"

# Iterate over each file in the target directory
# You can adjust the file pattern (*) as needed (e.g., *.txt for text files)
for file in "$TARGET_DIR"/*; do
    # Check if it's a regular file
    if [ -f "$file" ]; then
        FILENAME=$(basename "$file")
        # Add the separator line
        echo "///////////////////////////// $FILENAME" >> "$OUTPUT_FILE"
        
        # Optionally, you can handle different file types here
        # For simplicity, this script assumes all files are text files
        cat "$file" >> "$OUTPUT_FILE"
        
        # Add a newline for readability (optional)
        echo -e "\n" >> "$OUTPUT_FILE"
    fi
done

echo "All files from '$TARGET_DIR' have been concatenated into '$OUTPUT_FILE'."
