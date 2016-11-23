
import time

def getlastyearweekdayforyear(year):
    tm = time.strptime("31/12/" + str(year) +" 00:00:00", "%d/%m/%Y %H:%M:%S")
    return time.strftime("%A", tm)


if __name__ == "__main__":
    cyear = int(time.strftime("%Y", time.localtime()))
    for year in range(cyear - 60, cyear + 1):
        dayname = getlastyearweekdayforyear(year)
        print(str(year) + " - " + dayname)


