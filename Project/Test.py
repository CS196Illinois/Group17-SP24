from OrbitSystemClass import OrbitSystem
   
meep = OrbitSystem(1,5,1)
print(meep)
meep.addparticle(100000,0,1,2,3)
print(meep.initalconditions())
meep.runsim()
meep.writecsv("cat",0)