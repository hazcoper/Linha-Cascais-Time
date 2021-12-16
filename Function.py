
import datetime

def IsWeekend(dtime):
    """
    return if given date is a weekend or not
    """

    return True if dtime.weekday() >= 6 else False   #returns the day of the week, 0 is monday


def IsHoliday(dtime, holidaylist):
    """
    returns if given date is a holiday or not
    """

    month = dtime.month
    day = dtime.day

    return (month in holidaylist and holidaylist[month] == day)



def DealTime(time, isholiday, timetable):
    """
    time is in hh:mm
    Receive a time and a holiday flag and return how many minutes until the next train
    """

    
    hour = time.split(":")[0]
    minute = time.split(":")[1]

    if isholiday:
        flag = "f"
    else:
        flag = "n"

    if hour not in timetable[flag] or str((int(hour) + 1)%24) not in timetable[flag]:

        return -100
    
    option1 = timetable[flag][hour]
    minOp1 = ""

    for temp in option1:
        if int(minute) <= int(temp):
            minOp1 = temp
            break
    
    if minOp1 == "":
        hour = str((int(hour) + 1) %24)
        
        # while(hour not in timetable[flag]):
        #     hour = str((int(hour) + 1) %24)
        #     minutesToAdd += 60

        return (int(minute)-int(timetable[flag][hour][0]))%60
    else:
        
        return int(minOp1)-int(minute)

def GetClosest(timetable, holidaylist, mydate=None):
    """
    Returns the closest train using all the variables above
    """

    if mydate == None:
        #use now
        mydate = datetime.datetime.now()
    
    mytime = f"{mydate.hour}:{mydate.minute}"
    nextRequest = 60 - mydate.second

    if IsHoliday(mydate, holidaylist) or IsWeekend(mydate):
        return {"next-train": DealTime(mytime, True, timetable), "next-request": nextRequest}
    
    return {"next-train": DealTime(mytime, False, timetable), "next-request": nextRequest}


