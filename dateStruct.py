class DateStruct:
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__date = f"{day}/{month}/{year}"
    
    def get_day(self):
        return self.__day
    
    def get_month(self):
        return self.__month
    
    def get_year(self):
        return self.__year
    
    def get_date(self):
        return self.__date

    def set_day(self, day):
        if (day <= 30 and day >0):
            self.__day = day
            date_destruct = self.__date.split("/")
            self.__date = f"{day}/{date_destruct[1]}/{date_destruct[2]}"

    def set_month(self, month):
        if (month <= 12 and month > 0):
            self.__month = month
            date_destruct = self.__date.split("/")
            self.__date = f"{date_destruct[0]}/{month}/{date_destruct[2]}"
    
    def set_year(self, year):
        if (year <= 9999):
            self.__year = year
            date_destruct = self.__date.split("/")
            self.__date = f"{date_destruct[0]}/{date_destruct[1]}/{year}"