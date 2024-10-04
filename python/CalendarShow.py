import calendar
from datetime import date


class CalendarShow:
    def __init__(self) -> None:
        pass

    def calendarShow(self, year, month):
        print(calendar.month(year, month))

    def calculateDays(self, firstDay, secondDay):
        f_date = date(firstDay[0], firstDay[1], firstDay[2])
        s_date = date(secondDay[0], secondDay[1], secondDay[2])

        diff = s_date - f_date

        print(diff)
        print(diff.days)


ca = CalendarShow()
ca.calendarShow(2024, 8)
ca.calculateDays((2014, 7, 2), (2014, 7, 11))
