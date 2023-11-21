# Level Up: Advanced Python 
This is the repository for the LinkedIn Learning course Level Up: Advanced Python. The full course is available from [LinkedIn Learning][lil-course-url].

![Level Up: Advanced Python ][lil-thumbnail-url]

Python has quickly become one of the most popular programming languages in the world. If you’re looking to land a new role or stand out from the rest of the crowd, you need to develop your advanced coding skills. Discover integrated Python coding challenges to test your understanding of advanced Python concepts, following along with instructor Jonathan Fernandes, a results-driven data science consultant. Find out more about what it takes to bridge your knowledge gap to the next level, learning how to write highly advanced, production-level code that’s clean, effective, and dynamic. Upon completing this course, you’ll be prepared to leverage your new coding skills in your current or future role.<br><br>This course is integrated with GitHub Codespaces, an instant cloud developer environment that offers all the functionality of your favorite IDE without the need for any local machine setup. With GitHub Codespaces, you can get hands-on practice from any machine, at any time—all while using a tool that you’ll likely encounter in the workplace.<br><br>Each installment of the <em>Level Up</em> series offers at least 15 bite-sized opportunities to practice programming at various levels of difficulty, so you can challenge yourself and reinforce what you’ve learned. Check out the [Using GitHub Codespaces with this course][gcs-video-url] video to learn how to get a codespace up and running.

### Instructor

Jonathan Fernandes

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/jonathan-fernandes).

[lil-course-url]: https://www.linkedin.com/learning/level-up-advanced-python
[lil-thumbnail-url]: https://cdn.lynda.com/course/3213390/3213390-1667864247408-16x9.jpg
[gcs-video-url]: https://www.linkedin.com/learning/level-up-advanced-python/using-github-codespaces-with-this-course


# ANSWERS

## average_race_time.py

In this challenge, given a log of race times determine the average race time for Jennifer Rhines, who’s an American long distance runner.

### Requirements:
- Update average_race_time.py:
    - Complete the get_rhines_times() function, which returns a list of Jennifer Rhines’ race times.
    - Complete get_average() function which returns, Jennifer Rhines’ average race time.
    - See the function docstrings for details of the format of the return values.

``` python
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
```