from OrbitSystemClass import OrbitSystem
from GraphingClass import Graphing
from Constants import *

""""
This file gives preset systems for 
GraphingClass visual troubleshooting

The following are standard test systems:
- triangle 
- linear2
"""

def triangle():
    """3 particles in triangle with no velocity"""
    meep = OrbitSystem(1,1000,60)
    meep.addparticle(1000,1,0,0,0)
    meep.addparticle(9000,0,0,0,0)
    meep.addparticle(2000,0,1,0,0)
    print(meep.initalconditions())
    meep.runsim()

    plot = Graphing()

    # for i in range(meep.numberofparticle):
    #     print(meep.writedf(i))

    for i in range(meep.numberofparticle):
        plot.add_df(meep.writedf(i))
    
    plot.show()

def linear2():
    """2 colinear particles with no velocity
    - displays a weird behavior, notice y value scale (e-23)
    """
    meep = OrbitSystem(1,1000,60)
    meep.addparticle(1000,1,0,0,0)
    meep.addparticle(9000,0,0,0,0)
    print(meep.initalconditions())
    meep.runsim()

    plot = Graphing()

    for i in range(meep.numberofparticle):
        plot.add_df(meep.writedf(i))
    
    plot.show()

def sun_earth():
    """Sun and Earth system"""
    meep = OrbitSystem(HOUR,YEAR // HOUR, DAY // HOUR)
    meep.addparticle(SOLAR_MASS,0,0,0,0)
    meep.addparticle(EARTH_MASS,AU,0,0,EARTH_ORBITAL_VEL)
    print(meep.initalconditions())
    meep.runsim()

    plot = Graphing()

    for i in range(meep.numberofparticle):
        plot.add_df(meep.writedf(i))
    
    plot.show()

def sun_moon_earth():
    """Sun, earth, and moon system
    - assumes circular orbits
    - takes long time to run
    """
    meep = OrbitSystem(1,YEAR, HOUR)
    meep.addparticle(SOLAR_MASS,0,0,0,0)
    meep.addparticle(EARTH_MASS,AU,0,0,EARTH_ORBITAL_VEL)
    meep.addparticle(LUNAR_MASS,AU + LUNAR_EARTH_DISTANCE, 0, 0, LUNAR_ORBITAL_VEL)
    print(meep.initalconditions())
    meep.runsim()

    plot = Graphing()
    for i in range(meep.numberofparticle):
        plot.add_df(meep.writedf(i))
    
    plot.show()

def earth_moon():
    """Earth and Moon system
    - assumes circular orbits
    - not working well
    """
    meep = OrbitSystem(1,DAY, 1)
    meep.addparticle(EARTH_MASS, 0, 0, 0, 0)
    meep.addparticle(LUNAR_MASS, LUNAR_EARTH_DISTANCE, 0, 0, LUNAR_ORBITAL_VEL)
    print(meep.initalconditions())
    meep.runsim()

    plot = Graphing()
    for i in range(meep.numberofparticle):
        plot.add_df(meep.writedf(i))
    
    plot.show()
