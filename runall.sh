#!/bin/bash

# Loop through each data file, but only the xlsx and csv ones (ignore .md and others)
for file in "data"/*; do
    if [[ $file == *.csv || $file == *.xlsx ]]; then
        python pii.py "$file"
    fi
done