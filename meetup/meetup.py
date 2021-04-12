from datetime import date, timedelta

position = ["last", "1st", "2nd", "3rd", "4th", "5th"]


def meetup(year, month, week, day_of_week):
    start, end = date(year, month, 1), add_month(year, month)
    days = find_days(start, end, day_of_week)
    if week == "teenth":
        day = list(filter(lambda date: date.day in range(13, 20), days))[0].day
        return date(year, month, day)
    else:
        try:
            day = days[position.index(week) - 1].day
            return date(year, month, day)
        except:
            raise MeetupDayException()


def add_month(year, month):
    if month == 12:
        end_month = 1
        end_year = year + 1
    else:
        end_month = month + 1
        end_year = year

    return date(end_year, end_month, 1)


def find_days(start, end, day):
    return [d for d in daterange(start, end) if d.strftime("%A") == day]


def daterange(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)


class MeetupDayException(Exception):
    """Exception raised for errors in the week argument."""

    def __init__(self, message="Error: The day your are looking for doesnt exist"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"