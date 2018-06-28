import "BaseOrg.py"

if __name__ == "__main__":
    print ("Main")
else:
    MStartTime = datetime.datetime(year=2000,month=1,day=1,hour=0, minute=0)
    TimeStep = 60 #minutes per step
    GlblEIDS = EmployeeIDs(100,10000)
    GlblClock = WorldClock(TimeStep,epoch=MStartTime) 
    GlblShift = ShiftTypes(GlblClock)
    GlblShift.LoadDefault()
    NumEmps = 20
    mybase = BaseOrg(1,NumEmps,GlblEIDS,GlblClock,GlblShift)
    mypanm = PanamaOrg(2,NumEmps,GlblEIDS,GlblClock,GlblShift)
    mycomp = BaseOrg(3,NumEmps,GlblEIDS,GlblClock,GlblShift,stype="Compressed")

    for n in range(14*24):
        GlblClock.Step()
        mybase.step()
        mypanm.step()
        mycomp.step()