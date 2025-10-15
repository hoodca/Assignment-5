# Assignment-5
This Python script processes a CSV file containing COVID-19-related data and identifies the top 5 states with the highest number of deaths. It handles various data issues such as missing fields, malformed rows, and file-related errors.

How It Works:
Reads the file and strips whitespace.
Parses the data rows and extracts: 
State code,
Death count.

Handles missing or malformed values:
Missing death counts are treated as 0,
Ignores rows with incomplete data,
Aggregates total deaths per state,
Sorts states by death count in descending order,
Returns the top 5 states.

Example Usage

Run the script from the terminal:
python top_states_by_deaths.py

You’ll see output like:
Top 5 States by COVID-19 Death Count

NY: 58,743 deaths
CA: 53,221 deaths
TX: 47,890 deaths
FL: 35,670 deaths
PA: 27,104 deaths

Function Reference
get_top_states_by_death_count(file_path, file_encoding='utf-8')

Parameters:
file_path (str): Path to the CSV file.
file_encoding (str, optional): Encoding used to read the file (default 'utf-8').
Returns:
List of top 5 states as (state_code, death_count) tuples.

Error Handling
The script gracefully handles:
Missing file (FileNotFoundError)
Bad encoding (UnicodeDecodeError)
Malformed rows or missing columns
Non-integer or null death values
If no valid data, returns ([], 0).
