# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()

    # use list comprehension to extract race times
    rhines_racetimes = [
        re.search(r'(\d{2}:\d{2}(\.\d+)?)', line).group(1)
        for line in races.splitlines() if 'Jennifer Rhines' in line
    ]

    return rhines_racetimes

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    
    # Define a lambda function to convert a race time string to timedelta
    convert_to_timedelta = lambda racetime: datetime.timedelta(
        minutes=int(racetime.group('mins')),
        seconds=int(racetime.group('secs')),
        milliseconds=int(racetime.group('ms')) if racetime.group('ms') else 0
    )

    # Use map to apply the lambda function to each race time
    timedelta_list = list(map(convert_to_timedelta, (
        re.match(r'(?P<mins>\d{2}):(?P<secs>\d{2})(?:\.(?P<ms>\d+))?', racetime)
        for racetime in racetimes
    )))

    # calculate the total time using sum on the list
    total = sum(timedelta_list, datetime.timedelta())

    return f'{total / len(racetimes)}'[2:-5]