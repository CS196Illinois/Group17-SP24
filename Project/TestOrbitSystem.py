"""" 
This file tests only the OrbitSystemClass
"""
from OrbitSystemClass import OrbitSystem

meep = OrbitSystem(1,5,1)
print(meep)
meep.addparticle(100000,0,1,2,1)
meep.addparticle(200000,0,1.2,1000,3)
meep.addparticle(200000,0,100,1000,3)
meep.addparticle(200000,0,200,1000,3)
print(meep.initalconditions())
meep.runsim()

for i in range(meep.numberofparticle):
    print(meep.writedf(i))
print(type(meep.writedf(0).iloc[0]))

