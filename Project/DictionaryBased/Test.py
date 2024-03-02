from OrbitSystemClass import OrbitSystem
from Constants import *

meep = OrbitSystem(1,5,1)
print(meep)
meep.addparticle(100000,0,1,2,3)
meep.addparticle(1000000,5,13,22,35)
meep.addparticle(1000000,15,135,222,355)
print(meep.initalconditions())
meep.runsim()
meep.writecsv("cat",0)

#cat = OrbitSystem(60 * 60, 365 * 24, 24)
#cat.addparticle(SolarMass,0,0,0,0)
#cat.addparticle(EarthMass,AU,0,0,EarthOrbitalVel)
#print(cat.initalconditions())
#cat.runsim()
#cat.writecsv("null", 1)