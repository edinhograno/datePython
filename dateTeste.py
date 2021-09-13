from dateModel import DateModel

class DateTest():
    date = DateModel
    date.readDate()
    check = date.checkDate("20/05/2021")
    print(check)
    check = date.checkDate("45/58/5454")
    print(check)
    check = date.checkLeapYear("30/04/2003")
    print(check)
    check = date.checkLeapYear("30/04/2004")
    print(check)
    date.checkEaster(2012)
    date.write("30/04/1991")