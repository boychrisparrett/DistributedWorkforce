import numpy as np
import datetime

class WorkShift:
    def __init__(self,n,clock):
        self.typename = n
        self.hours = 0
        self.start_time = 0
        self.stop_time = 0
        self.dutydays = []
        self.weeklyhrs = 0
        self.wrldclock = clock
        
    def setStartStopTime(self,start_dt,stop_dt):
        self.start_time = start_dt
        self.stop_time = stop_dt
        self.hours = (self.stop_time - self.start_time).total_seconds() / 3600
        
    def setDutyDays(self,dd):
        self.dutydays = dd
        self.weeklynorm = len(dd) * self.hours
    
    def isDutyDay(self,cur_t=None):
        if cur_t == None: cur_t = self.wrldclock.getDTG()
        ppday = self.wrldclock.getPPDay()
        
        if (ppday in self.dutydays) and cur_t.time() >= self.start_time.time() and cur_t.time() < self.stop_time.time():
            return True
        elif (self.stop_time.day > self.start_time.day):
            if (ppday in self.dutydays) and cur_t.time() >= self.start_time.time() and cur_t.time() < datetime.time(hour=23,minute=59):
                return True
            else:
                if ppday == 0: ppday = 13
                if ppday in self.dutydays and cur_t.time() < self.stop_time.time():
                    return True
        else:
            return False
        
        return False        