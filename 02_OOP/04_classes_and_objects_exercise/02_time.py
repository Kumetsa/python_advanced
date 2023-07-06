class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)

    def next_second(self) -> str:
        new_seconds = self.seconds + 1
        new_minutes = self.minutes
        new_hours = self.hours

        if new_seconds > Time.max_seconds:
            new_seconds = 0
            new_minutes += 1

            if new_minutes > Time.max_minutes:
                new_minutes = 0
                new_hours += 1

                if new_hours > Time.max_hours:
                    new_hours = 0

        return Time(new_hours, new_minutes, new_seconds).get_time()


time = Time(9, 30, 59)
print(time.next_second())
