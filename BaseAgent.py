class BaseAgent:
    def __init__(self,uid,schd,t):
        self.__ID = uid             # Agent unique identifier
        self.__Schedule = schd
        self.__MaxHours = 80
        self.__Eod = t
        self.__CurOrg = 0
        self.__CurOrgDwell = 0
        self.__StartTime = t        # Organization time that the agent was created
        self.__StopTime = -1        # Organization time that the agent was stopped
        self.__Effort = 0           # Actual effort put forth by agent by year
        self.__Talent = 0           # The natural ability to do something (talent) 
        self.__Affectivity = 0      # Intrinsic emotional outlook on life
        self.__Salary = 0           # The amount the employee gets paid
        self.__SelfPerception = 0   # The self-bias the employee has on itself & environment
        self.__JobSatisfaction = 0  # How content an individual is in a job
        self.__EnvPerception = 0    # The perceived culture of agent's surroundings
        self.__status = 0           # Agent state in terms of Fired, Active, or Promoted

    ############################################################################  
    # Memeber Attribute Set Routines
    def setStartTime(self,t): self.__StartTime = t
    def setStopTime(self,t): self.__StopTime = t
    def setCurOrg(self,i): self.__CurOrg = i
    def setCurOrgDwell(self,t): self.__CurOrgDwell = t
    def setSchedule(self,s): self.__Schedule = s
    def setEffort(self,i): self.__Effort = float(i)
    def setTalent(self,i): self.__Talent = float(i)
    def setAffectivity(self,i): self.__Affectivity = float(i)
    def setSalary(self,i): self.__Salary = i
    def setSelfPerception(self,i): self.__SelfPerception = float(i)
    def setJobSatisfaction(self,i): self.__JobSatisfaction = float(i)
    def setEnvPerception(self,i): self.__EnvPerception = float(i)
    def setStatus(self,s): self.__status = s

    ############################################################################  
    # Memeber Attribute Get Routines
    def getUID(self): return self.__ID
    def getStartTime(self): return self.__StartTime
    def getStopTime(self): return self.__StopTime
    def getCurOrg(self): return self.__CurOrg
    def getCurOrgDwell(self,t): return self.__CurOrgDwell
    def getSchedule(self): return self.__Schedule
    def getEffort(self): return self.__Effort
    def getTalent(self): return self.__Talent
    def getAffectivity(self): return self.__Affectivity
    def getSalary(self): return self.__Salary
    def getSelfPerception(self): return self.__SelfPerception
    def getJobSatisfaction(self): return self.__JobSatisfaction
    def getEnvPerception(self): return self.__EnvPerception
    def getStatus(self): return self.__status
    
    # Overload
    def Step(self):
        pass