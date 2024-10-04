class DaysInDays:
    def __init__(self, monthName):
        self.monthName = f"{monthName.capitalize()}"

    def daysofmonth(self):
        if self.monthName in ("January", "March", "May", "July", "August", "October", "December"):
            return 31
        elif self.monthName in ("April", "June", "September", "November"):
            return 30
        elif self.monthName == "February":
            return "28/29"
        else:
            return "Wrong month"


d = DaysInDays("february")
print(d.daysofmonth())

