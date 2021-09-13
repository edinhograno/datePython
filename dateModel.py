from dateStruct import DateStruct

class DateModel(DateStruct):
    def readDate():
        date = input("Type a date dd/mm/yyyy: ")
        return date

    def checkDate(date):
        date_destruct = date.split("/")
        day = date_destruct[0]
        month = date_destruct[1]
        year = date_destruct[2]

        day_check = 0
        month_check = 0
        year_check = 0

        try:
            day_check = 1 if int(day) <= 30 and int(day) > 0 else 0
            month_check = 1 if int(day) <= 30 and int(day) > 0 else 0
            year_check = 1 if int(day) <= 30 and int(day) > 0 else 0

            if (day_check == 1 and month_check == 1 and year_check == 1): return 1
            else: return 0
        except ValueError as error:
            input("Something is wrong, try again! [Press enter]")

    def checkLeapYear(date):
        date_destruct = date.split("/")
        year = date_destruct[2]

        if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
            return 1
        else:
            return 0 
    
    def checkEaster(year):
        x = (19 * (year % 19) + 24) % 30
        y = (2 * (year % 4) + 4 * (year % 7) + 6 * x + 5) % 7
        res = x + y

        if res > 9:
            day = res - 9
            month = 4
        else:
            day = res + 22
            month = 3
        return print(f"{day}/{month}/{year}")

    def write(date):
        try:
            write_month = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }
            date_destruct = date.split("/")
            day = date_destruct[0]
            month = date_destruct[1]
            year = date_destruct[2]

            print(f"{day} {write_month[int(month)]} {year}")
            return 1
        except:
            return 0
        