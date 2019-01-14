# southwest-flight-count-scraper

*Project Description*
Southwest Airlines Flight Count Data Scraper
Created by George Thompson

This data scraper will allow users to retrieve the count of available "one-stop" and "non-stop"
flights given origin and destination locations within a provided CSV file.

*File Guide*
Script: southwest-flight-count-scraper.py
Input: example-input.csv
Output: output.csv

*Additional Comments & Concerns*
Since this program was created for solely myself to complete a job, the program
was built under the assumption that the user will not make errors when prompted for information. 
Error handling was not implemented in this project for this reason.

*Running the script*
Step 1: place both the "example-input.csv" and "southwest-flight-countscraper.py" files into the
same folder.

Step 2: open your local terminal and cd into the folder that you placed your files

Step 3: 
Run "python example-input.csv" or
Run "python3 example-input.csv" (this is dependent on your OS, you need Python3 to run this script)

Step 4:
Enter the information requested by the program. If you make any errors, press "ctrl+c" and start 
from the beginning.

*additional comments*
Finally, some TODO's are scattered throughout the script for potential improvements I'll make if I
happen to revisit this project. Otherwise, this program achieves its purpose even though some code
could be written more elegantly.

WARNING: The test CSV has a limited number of flights, so it's very possible that Southwest's site
will eventually block your IP from further running searches. I plan to first learn Scrapy before 
handling such issues in future webscraping projects.

WARNING: This was built in a Linux distribution, so the shebang line will need to be changed to run
this in OS X or Windows. Furthermore, my distribution's terminal would not copy the CSV file path
when dragging it onto it. If that the case, CD into the directory with the CSV and Python script,
then simply type the CSV file's name when prompted.
