#!/bin/bash

echo "Running Gamma Calculator..."
cd modules

echo "Downloading spx_quotedata.csv..."
# Run getSPXData.py
python getSPXData.py &
wait $!
downloaded_file=$(find ~/Downloads -name 'spx_quotedata.csv*' | head -n 1)
if [ -f "$downloaded_file" ]; then
    mv "$downloaded_file" spx_quotedata.csv
fi
echo "Successfully downloaded spx_quotedata.csv!"

directory_path="../saved_plots"
rm -rf "$directory_path"/*
echo "saved_plots contents cleared."

# Run main.py
echo "Creating Absolute Gamma Exposure and Gamma Profile Charts..."
python main.py &
main_pid=$!  # Assign the process ID to $main_pid
saved_plots_dir="saved_plots"
last_modified_file="last_modified.txt"

while true; do
    new_image=$(find "../saved_plots" -type f -name '*.png' -printf "%T@ %p\n" | sort -n | tail -n 1 | cut -f2- -d' ')
    last_modified=$(cat "../last_modified.txt")

    if [ -f "$new_image" ] && [ "$new_image" != "$last_modified" ]; then
        echo "Opening new image: $new_image"
        start "" "$new_image"
        echo "$new_image" > "../last_modified.txt"
    fi

    # Check if main.py has finished
    if ! ps -p $main_pid > /dev/null; then
        break  # Break out of the loop if main.py has finished
    fi

    sleep 1
done

echo "Successfully created Absolute Gamma Exposure and Gamma Profile Charts!"
sleep 3
echo "Closing gammaCalculator.sh..."
sleep 3