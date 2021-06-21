class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        h, m = self.clock_time()
        return f"{self.format_unit(h)}:{self.format_unit(m)}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        self.minute += minutes
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        return self

    def clock_time(self):
        h, m = divmod(self.minute, 60)
        clock_hour = (self.hour + h) % 24
        return (clock_hour, m)

    def format_unit(self, unit: int) -> str:
        return str(unit).rjust(2, "0")
