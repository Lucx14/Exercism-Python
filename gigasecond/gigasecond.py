from datetime import timedelta

gigasecond = timedelta(seconds=10 ** 9)


def add(moment):
    return moment + gigasecond
