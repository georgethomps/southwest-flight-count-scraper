# SECTION 0: IMPORTING MODULES

# import csv & beautifulsoup modules
import csv, bs4

# import selenium modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# SECTION 1: IMPORTING & BUILDING DATA

# ask user for csv file
csv_file = input('Please enter the name of your CSV file and press enter...\n')

# open CSV file and store flight destinations
with open(csv_file) as flight_table:
    flight_data = list(csv.reader(flight_table))
    flight_data = flight_data[1:]
flight_table.close()

# prompt user for departure and return dates
dept_date = input('\nPlease enter the target departure date in the following format: YYYY-MM-DD\n')
rtn_date = input('\nPlease enter the target return date in the following format: YYYY-MM-DD\n')

# create list of dictionaries w/ flight info
def create_flight_data(data):
    '''Takes the list of flight destinations and creates a list
    of dictionaries that contain the origin, destination, departure
    and return dates, and count of one-stop and non-stop flights
    '''

    # define global constants
    global dept_date
    global rtn_date

    # declare flight data list
    flights = []

    # loop through destination data and append to flight data
    for destination in data:

        # separate flight destinations and add pair to flight data
        pair = destination[0]
        flights.append({'origin': pair[:3], 'destination': pair[4:],
                        'departure': dept_date, 'return': rtn_date,
                        'oneStop_count': '', 'nonStop_count': ''})
    
    # return flight data
    return flights

# create flight data
flights = create_flight_data(flight_data)


# SECTION 2: WEBSCRAPE & STORE FLIGHT COUNTS

# open webdriver before looping & set wait time
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# search link function 
def create_search(origin, destination, dept_date, rtn_date):
    '''creates the url that the browser will open to perform the 
    flight search given two destinations and return/departure dates
    '''
    link = 'https://www.southwest.com/air/booking/select.html?originationAirportCode=~~~&destinationAirportCode=***&returnAirportCode=&departureDate=+++&departureTimeOfDay=ALL_DAY&returnDate=@@@&returnTimeOfDay=ALL_DAY&adultPassengersCount=1&seniorPassengersCount=0&fareType=USD&passengerType=ADULT&tripType=roundtrip&promoCode=&reset=true&redirectToVision=true&int=HOMEQBOMAIR&leapfrogRequest=true'
    link = link.replace('~~~', origin).replace('***',destination).replace('+++',dept_date).replace('@@@',rtn_date)
    return link

# flight counting function
def count_flights(soup_matches):
    '''searches a beautifulsoup object of CSS element matches
    and counts flights if the element text indicates the flight
    is a one-stop or non-stop flight.
    '''
    # TODO: incorporate listcomp?
    # create variables to store flight counts
    oneStop_count = 0
    nonStop_count = 0

    # loop through beautifulsoup matches
    for match in soup_matches:

        # count 1 stop & nonstop flights
        if match.text == '1 stop':
            oneStop_count += 1
        elif match.text == 'Nonstop':
            nonStop_count += 1

    # return a tuple of the flight count categories
    return oneStop_count, nonStop_count

# notify user that flight count data is being retrieved
print('Retrieving and storing flight count data...\n')

# loop through flights and record flight count data
# TODO: put this into a separate module
for flight in flights:

    # set search criteria
    # TODO: make this more elegant
    origin = flight['origin']
    destination = flight['destination']
    dept_date = flight['departure']
    rtn_date = flight['return']

    # string together search
    link = create_search(origin, destination, dept_date, rtn_date)

    # open link with webdriver
    driver.get(link)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    # move to next flight if no flights exist
    result_test = soup.find('title')

    if result_test.text == 'Southwest Airlines - Book a Flight':
        flight['oneStop_count'] = 0
        flight['nonStop_count'] = 0
        continue

    # wait for the "see-packages" css class to be available before 
    # creating the beautifulsoup object
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.see-packages')))
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    # store css classes for "1 stop" & "Nonstop" flights
    # TODO: remove this from the loop
    css_classes = ['flight-stops-badge select-detail--flight-stops-badge', 
                'flight-stops-badge flight-stops-badge_nonstop select-detail--flight-stops-badge']

    # find all "1 stop" and "nonstop" flights
    matches = soup.find_all('div', {'class': [css_classes[0], css_classes[1]]})

    # store results in dictionary
    flight['oneStop_count'], flight['nonStop_count'] = count_flights(matches)

# close webdriver
driver.close()

# notify user flight counts were successfully retrieved
print('\nFlight count data successfully retrieved!\n')


# SECTION 3: WRITE FLIGHT COUNT DATA TO OUTPUT CSV FILE

# notify user that the data is being exported
print('\nExporting Data...\n')

# create a list of table column names for the CSV file
col_headers = list(flights[0].keys()); col_headers = [x.replace("_"," ").title() for x in col_headers]

# create new CSV file with the count data
# TODO: make this a function
# TODO: create a notification message TODO: finish this part!
with open('output.csv','w') as output_file:
    
    # create CSV writer
    writer = csv.writer(output_file, delimiter = ',')

    # write column headers
    output_file.write(','.join(col_headers)); output_file.write('\n')
    
    # add row entries for all flights
    for flight in flights:
        row = [str(values) for values in flight.values()]
        writer.writerow(row)

output_file.close()

# notify user that the data was successfully exported
print('\nData successfully exported!\n')

# close the program while notifying the user
print('\nTerminating program...')
quit()
