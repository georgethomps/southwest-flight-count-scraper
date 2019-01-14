# southwest-flight-count-scraper

**Project Description**

This data scraper will allow users to retrieve the count of available "one-stop" and "non-stop"
flights given origin and destination locations within a provided CSV file.  

&nbsp;

**File Guide**

Script: `southwest-flight-count-scraper.py`

Input: `example-input.csv`

Output: `output.csv`

&nbsp;

**Additional Comments & Concerns**

This program is built under the assumption that the user will not make errors 
when prompted for information; error-handling is not implemented within this script.

The input CSV file can be named whatever you want and contain any destinations you want
as long as the file has a column header, the flights are separated by a hyphen ("-"), and
the destinations are only airport codes.

*WARNING*: The test CSV has a limited number of flights, so it's very possible that Southwest's site
will block your IP if you run too many searches. If you experience issues, reduce the number
of rows in the input CSV file.

&nbsp;

**Running the Script**

1. place both the "example-input.csv" and "southwest-flight-countscraper.py" files into the
same folder.

2. open your local terminal and cd into the folder that you placed your files

3. Run "python example-input.csv" or run "python3 example-input.csv" (this is dependent on your OS, you need Python 3 to run this script)

4. Enter the information requested by the program. If you make any errors, press "ctrl+c" and start 
from the beginning.

&nbsp;


