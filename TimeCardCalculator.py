from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

class timeCalculator:
    def __init__(self):
        
        self.currentWorked = 0  #current hours worked

    def tConvertToTime(self, time):
        self.hours = ''
        self.min = ''

        count = 0
        for i in time:
            if i != ':':
                if count < 2:
                    self.hours = self.hours + time[count]
                if count >= 2:
                    self.min = self.min + time[count]
            count = count + 1
        
        if int(self.hours) > 40:
            self.hours = int(self.hours) - 40

        return (int(self.hours) * 60) + int(self.min)


    def getTimeRemainingToday(self):
        #get the total Min left that i need to work today 
        #get the day of the week 
        weekDay = date.weekday(datetime.now())
        
        #subtract the amount of hours needed for an 8 hr workday, depending on what day of the week it is, to calculate how many hours need to be worked today. 
        if weekDay == 0:
            remaning = (8 * 60) - int(self.currentWorked)
        elif weekDay == 1:
            remaning = (16 * 60) - int(self.currentWorked)
        elif weekDay == 2:
            remaning = (24 * 60) - int(self.currentWorked)
        elif weekDay == 3:
            remaning = (32 * 60) - int(self.currentWorked)
        elif weekDay == 4:
            remaning = (40 * 60) - int(self.currentWorked)
        else:  
            remaining = 0
            print ('Why are you working on a weekend?')
        
        # see if I had a lunch break(before noon), if not, add 30 min to remaining time 
        now = datetime.now()
        noon = now.replace(hour=12, minute=0, second=0, microsecond=0) 
        if now < noon:
            remaning = remaning + 30

        return timedelta(minutes= remaning)

    def setCurrentTotalTime(self, currentHrs):
                                   
        currentTime = self.tConvertToTime(currentHrs)        
        #assigned total hours worked(in min) to gloabal variable currentWorked    
        self.currentWorked = currentTime
       
        

    def leaveTime(self):       
        #subtract worked time from total time 
        now = input('what time was the last time you punched in? ' )
        upDatedTime = self.tConvertToTime(now)
    
        print ('\nTime clocked in:\n%10s' % (str(timedelta(minutes = upDatedTime))))

        #add the time from the last timecard punch-in to current worked   
       # hoursLeft = datetime.now() - timedelta(minutes= upDatedTime)
       # hoursLeft = hoursLeft + timedelta(minutes= self.currentWorked)
        
       # print ( 'Current hours worked this week:\t ' + hoursLeft.strftime("%I:%M"))
        newUpdateTime = timedelta(minutes = upDatedTime) + self.getTimeRemainingToday()      
        
        return str(newUpdateTime)

def main():
    timeCard = timeCalculator()

    
    while 1:
        curHrs = str(input('Current total hours:minuites (ex: 21:23) worked: '))
        timeCard.setCurrentTotalTime(curHrs)
       
        print()
        print ('It is Now:\n%10s'  % (datetime.now().strftime('%X')))
        print ('I go home today at:\n%10s ' % (timeCard.leaveTime()))
		
		
        key = input('\nPress Y to calculate again or Q to quit: ')

        if key == 'q' or key == 'Q':
            return
  
if __name__ == '__main__':

    main()