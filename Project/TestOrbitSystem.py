from OrbitSystemClass import OrbitSystem
"""" 
This file tests only the OrbitSystemClass
"""


meep = OrbitSystem(1,5,1)
print(meep)
meep.addparticle(100000,0,1,2,1)
meep.addparticle(200000,0,1.2,1000,3)
meep.addparticle(200000,0,100,1000,3)
meep.addparticle(200000,0,200,1000,3)
print(meep.initalconditions())
meep.runsim()
#meep.writecsv("cat",0)
# print(meep.writedf(0))
# print(meep.writedf(1))
# print(meep.writedf(2))
# print(meep.writedf(3))

for i in range(meep.numberofparticle):
    print(meep.writedf(i))
print(type(meep.writedf(0).iloc[0]))

