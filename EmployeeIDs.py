import numpy as np

class EmployeeIDs:
    def __init__(self,initnum,maxnum,minnum=0):
        self.eids = np.random.randint(minnum,maxnum,initnum)
    
    def getEID(self):
        nid = self.eids[0]
        self.eids = np.delete(self.eids,0)
        return nid
    
    def EIDExists(self,eid): return not (eid in self.eids)
        