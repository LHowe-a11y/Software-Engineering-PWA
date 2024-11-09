
def monthname(currentmonth):
    match currentmonth:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"
def date(year,month,day):
    return str(year+zeroadder(month)+zeroadder(day))
def zeroadder(x):
    match x:
        case 1:
            return "01"
        case 2:
            return "02"
        case 3:
            return "03"
        case 4:
            return "04"
        case 5:
            return "05"
        case 6:
            return "06"
        case 7:
            return "07"
        case 8:
            return "08"
        case 9:
            return "09"
        case _:
            return str(x)
with open("myPWA\.database\FormattedDates.txt", "w") as w:
    year = "2025"
    month = 1
    day = 1
    monthdays = 31
    id = 1
    while True:
        w.write("("+str(id)+","+date(year,month,day)+",'"+monthname(month)+" "+str(day)+"'),\n")
        day += 1
        id += 1
        if day > 28:
            if day == 29 and month == 2:
                day = 1
                month = 3
            elif day == 31:
                if month == 9 or month == 4 or month == 6 or month == 11:
                    day = 1
                    month += 1
            elif day == 32:
                if month == 12:
                    break
                else:
                    day = 1
                    month += 1
    w.close()