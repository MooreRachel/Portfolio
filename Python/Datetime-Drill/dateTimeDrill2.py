####found help in tutorial at http://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/

from datetime import datetime
from pytz import timezone

## is office open or closed
#officeHrs: 9am to 9pm

##UTC Time
nowUTC = datetime.now(timezone('UTC'))

##formatting the time
timeFormat = " %I:%M %p %a, %d %b %Y"

#Timezones - new timezones can be added here
locations = {
#'Enter Location ' :(nowUTC.astimezone(timezone('Enter timezone'))),
'Portland ': (nowUTC.astimezone(timezone('US/Pacific'))),
'New York ': (nowUTC.astimezone(timezone('US/Eastern'))),
'London   ': (nowUTC.astimezone(timezone('Europe/London'))),
'Tokyo    ': (nowUTC.astimezone(timezone('Asia/Tokyo')))}


def officeTime(locations):
    for key, value in locations.items():
        hr = value.strftime('%H')
        branch = key
        locationTime = value.strftime(timeFormat)
        if int(hr) >= 9 and int(hr) < 21:
            print "Open\t" + branch + locationTime
        else:
            print "Closed\t" + branch + locationTime
            
officeTime(locations)

#Olson Database 
##http://www.iana.org/time-zones

##check for accuracy
##http://www.timeanddate.com/worldclock/ uses the Olson Database
