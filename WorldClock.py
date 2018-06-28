import datetime

class WorldClock:
    WC = {0:"Mon",1:"Tue",2:"Wed",3:"Thr",4:"Fri",5:"Sat",6:"Sun"}
    def __init__(self,tstep,epoch=None,tz=None):
        self.epoch = epoch
        self.tz = tz
        if self.epoch is None:
            self.epoch = datetime.datetime.now(tz)
        self.curtime = self.epoch
        self.tstep = tstep
        self.yweek = 0
        self.shftweek = 0
        self.tick = 0
        
    def Step(self): 
        self.curtime = self.curtime + datetime.timedelta(minutes=self.tstep)
        self.yweek = int(self.getJDay() / 7)
        self.shftweek = self.yweek % 2
        self.tick += 1
        
    #---- Get routines
    def getDTG(self): return self.curtime
    def getPPDay(self):return self.curtime.weekday() + self.shftweek * 7
    def getTick(self): return self.tick
    def getCurSecond(self): return self.curtime.second
    def getCurMinute(self): return self.curtime.minute
    def getCurHour(self): return self.curtime.hour
    def getCurDay(self): return self.curtime.day
    def getCurMonth(self): return self.curtime.month
    def getCurYear(self): return self.curtime.year
    def getCurWeekday(self): return self.curtime.year
    
    def isWeekDay(self): return self.curtime.isoweekday()
    def getJDay(self): return self.curtime.timetuple().tm_yday
 