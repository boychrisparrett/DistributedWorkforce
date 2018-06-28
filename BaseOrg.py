from BaseAgent import *
import numpy as np

class BaseOrg:
    def __init__(self,uid,n_emps,empids,clock,shfttypes,stype="Regular"):
        self.uid = uid
        self.wrldclock = clock
        self.shifttypes = shfttypes
        self.availempids = empids
        self.numemps = n_emps
        self.stats = {}  
        self.members = {}
        self.stype = stype
        self._LoadEmployees_()
        
    def _LoadEmployees_(self):
        #regular... overload function for different
        cur_t = self.wrldclock.getDTG()
        for n in range(self.numemps):
            nid = self.availempids.getEID()
            newagt = BaseAgent(nid,self.shifttypes.getShift(self.stype),cur_t)
            newagt.setCurOrg(self.uid)
            self.members[nid] = newagt
            self.stats[nid] = [0]
            
    def addMember(self, agtid, shift): 
        newagt = BaseAgent(agtid,self.shifttypes.getShift(shift),cur_t)
        newagt.setCurOrg(self.uid)
        self.members[newagt.getUID()] = newagt
        self.stats[nid] = []
        
    def delMember(self, agt): 
        if agt.getUID() in self.members.keys(): 
            agt.setCurOrg(None)
            self.members.pop(agt.getUID())
    
    def step(self):
        # Pass
        nmem = 0
        cur_t = self.wrldclock.getDTG()
        lmem = list(self.members.keys())
        np.random.shuffle(lmem)
        for m in lmem:
            if self.members[m].getSchedule().isDutyDay(cur_t):
                print("\t member",m," ON THE CLOCK",self.members[m].getSchedule().typename)
                self.stats[m].append(1)
            else:
                #print("\t member",m," off duty",self.members[m].schedule.typename)
                self.stats[m].append(0)