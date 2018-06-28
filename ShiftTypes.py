import datetime
from WorkShift import *

class ShiftTypes:
    def __init__(self,clock,shift_file=None):
        self.shifttype = {}
        self.glblclock = clock
        
    def LoadShiftSchedules(self):
        self.LoadDefault()
        
    def LoadDefault(self):
        self.shifttype["Panama_Team1_AM"] = WorkShift("Panama_Team1_AM",self.glblclock)
        self.shifttype["Panama_Team1_AM"].setStartStopTime(datetime.datetime(year=2000,month=1,day=1,hour=6, minute=0), 
                              datetime.datetime(year=2000,month=1,day=1,hour=18, minute=0))
        self.shifttype["Panama_Team1_AM"].setDutyDays([0,1,4,5,6,9,10])
        
        self.shifttype["Panama_Team1_PM"] = WorkShift("Panama_Team1_PM",self.glblclock)
        self.shifttype["Panama_Team1_PM"].setStartStopTime(datetime.datetime(year=2000,month=1,day=1,hour=18, minute=0), 
                              datetime.datetime(year=2000,month=1,day=2,hour=6, minute=0))        
        self.shifttype["Panama_Team1_PM"].setDutyDays([0,1,4,5,6,9,10])
        
        self.shifttype["Panama_Team2_AM"] = WorkShift("Panama_Team2_AM",self.glblclock)
        self.shifttype["Panama_Team2_AM"].setStartStopTime(datetime.datetime(year=2000,month=1,day=1,hour=6, minute=0), 
                              datetime.datetime(year=2000,month=1,day=1,hour=18, minute=0))
        self.shifttype["Panama_Team2_AM"].setDutyDays([2,3,7,8,11,12,13])
        
        self.shifttype["Panama_Team2_PM"] = WorkShift("Panama_Team2_PM",self.glblclock)
        self.shifttype["Panama_Team2_PM"].setStartStopTime(datetime.datetime(year=2000,month=1,day=1,hour=18, minute=0), 
                              datetime.datetime(year=2000,month=1,day=2,hour=6, minute=0))
        self.shifttype["Panama_Team2_PM"].setDutyDays([2,3,7,8,11,12,13])
        
        self.shifttype["Regular"] = WorkShift("Regular",self.glblclock)
        self.shifttype["Regular"].setStartStopTime(datetime.datetime(year=2000,month=1,day=1,hour=8, minute=0), 
                              datetime.datetime(year=2000,month=1,day=1,hour=16, minute=0))
        self.shifttype["Regular"].setDutyDays([0,1,2,3,4,7,8,9,10,11])
        
        self.shifttype["Compressed"] = WorkShift("Compressed",self.glblclock)
        self.shifttype["Compressed"].setStartStopTime(datetime.datetime(year=2000,month=1,day=1,hour=8, minute=0), 
                              datetime.datetime(year=2000,month=1,day=1,hour=18, minute=0))
        self.shifttype["Compressed"].setDutyDays([0,1,2,3,7,8,9,10])
        
    def getCurrShift(self,t):
        cur = None
        for i in self.shifttype.keys():
            if self.shifttype[i].isDutyDay(t):
                cur = self.shifttype[i]
        return cur
    
    def getShift(self,n): return self.shifttype[n]
