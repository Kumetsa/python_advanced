from datetime import datetime


class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        month, year = cls.get_month_and_year(date)

        return cls(name, id, int(year), month, age_restriction)

    @staticmethod
    def get_month_and_year(date):
        day, month, year = date.split(".")
        month_word = datetime.strptime(month, "%m").strftime("%B")

        return month_word, year

    def __repr__(self):
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"
