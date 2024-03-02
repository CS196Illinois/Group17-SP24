from OrbitSystemPandas import OrbitSystemdf
from Constants import *

# records as follows : seconds, amount of runs (at the previous amount)(so 60 sec * 60 min * 24 hour * 365 day), report amount (based off first)
# (every minute, every min for a year, every day)
cat = OrbitSystemdf(60 * 60, 365 * 24, 24)
cat.addparticle(SolarMass,0,0,0,0)
cat.addparticle(EarthMass,AU,0,0,EarthOrbitalVel)
print(cat.getsystem())

cat.runsim()
cat.writecsv("null", 1)