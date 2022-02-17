# json-merger
Simple python script for merging many json files into one single json with the contents of the individual files in a json list.

# How to use:
To use this script you need to change the file path in the `glob.glob()` function on line 16 to match the file path to your json files, as well as your file name pattern. The script is made for a file name pattern where the files are indexed with numbers. Once you get `glob.glob()` to successfully find your .json files, you need to update the split functions on line 19 to get the index from the `file.name`.

#Example files:

File name pattern: 0.json, 1.json, 2.json... etc.
