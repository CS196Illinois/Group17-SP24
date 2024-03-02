import math
import pandas as pd
import numpy as np

class OrbitSystemdf:
    def __init__(self, timeinterval : float, trialamount : int, reportinterval : int):
        # interval - delta t measurement(seconds) amount - number of intervals ran (#) report - number till reporting postition (#)
        self.timeinterval = timeinterval
        self.trialamount = trialamount
        self.reportinterval = reportinterval
        self.numberofparticle = 0
        self.systemdf = pd.DataFrame({"mass" : [], "x_pos" : [], "y_pos" : [], "x_vel" : [], "y_vel" : [], "x_acc" : [], "y_acc" : []}, dtype = np.float64)
        self.x_list = []
        self.y_list = []
        self.Grav = 6.6743*(10**-11)


    def addparticle(self, mass : np.float64, x_pos : np.float64, y_pos :np.float64, x_vel : np.float64, y_vel : np.float64):
        self.systemdf.loc[self.numberofparticle] = np.float64([mass, x_pos, y_pos, x_vel, y_vel, 0, 0])  # forces np.float64 type
        self.numberofparticle += 1

    def getsystem(self) :
        return self.systemdf
    
    def getinfo(self) :
        self.systemdf.info()

    def __findvector(self, particle_1 : int, particle_2 : int) :
        x_1 = self.systemdf.loc[particle_1, "x_pos"]
        x_2 = self.systemdf.loc[particle_2, "x_pos"]
        y_1 = self.systemdf.loc[particle_1, "y_pos"]
        y_2 = self.systemdf.loc[particle_2, "y_pos"]
    
        dx = x_2 - x_1
        dy = y_2 - y_1
        magnitude = (dx**2 + dy**2)**.5
        sine = math.asin(dy/magnitude)
        cosine = math.acos(dx/magnitude)
        if(sine >= 0) :
            theta = cosine
        elif(sine < 0) :
            theta = -cosine
    
        #print("vector for calculation", [magnitude, theta * 180/math.pi])
        return [magnitude, theta]

    # Force of Gravity of particle_2 on particle_1; m_2 is mass of particle 2
    def __gforce(self, particle_1 : int, particle_2 : int) :
        vector = self.__findvector(particle_1, particle_2)
        m_2 = self.systemdf.loc[particle_2, "mass"]
        acceleration = self.Grav*m_2/(vector[0])**2
        self.systemdf.loc[particle_1, "x_acc"] += acceleration*math.cos(vector[1])
        self.systemdf.loc[particle_1, "y_acc"] += acceleration*math.sin(vector[1])

    #iterates through every particle and applys gforce function
    def __apply_gforce(self) :
        for x in range(0,self.numberofparticle):
            for y in range (0,self.numberofparticle):
                if x != y:
                    self.__gforce(x, y)

    # can be swapped to do row opperations to calculate all positions in one command
    def __position(self, particle_1 : int) :
        x_vel = self.systemdf.loc[particle_1, "x_vel"]
        y_vel = self.systemdf.loc[particle_1, "y_vel"]
        x_acc = self.systemdf.loc[particle_1, "x_acc"]
        y_acc = self.systemdf.loc[particle_1, "y_acc"]
        dt = self.timeinterval

        self.systemdf.loc[particle_1, "x_pos"] += .5 * x_acc * (dt ** 2) + x_vel * dt 
        self.systemdf.loc[particle_1, "y_pos"] += .5 * y_acc * (dt ** 2) + y_vel * dt

    def __velocity(self, particle_1 : int) :
        x_acc = self.systemdf.loc[particle_1, "x_acc"]
        y_acc = self.systemdf.loc[particle_1, "y_acc"]
        dt = self.timeinterval

        self.systemdf.loc[particle_1, "x_vel"] += x_acc * dt
        self.systemdf.loc[particle_1, "y_vel"] += y_acc * dt

    def __resetacc(self, particle_1 : int) :
        self.systemdf.loc[particle_1, "x_acc"] = 0
        self.systemdf.loc[particle_1, "y_acc"] = 0

    # can possibly be replaced by 3-D xarray (or numpy) with time, particlenum and position values
    def __recordpos(self) :
        temp_x = []
        temp_y = []

        for particle in range(self.numberofparticle):
            temp_x.append(self.systemdf.loc[particle, "x_pos"])
            temp_y.append(self.systemdf.loc[particle, "y_pos"])
        
        self.x_list.append(temp_x)
        self.y_list.append(temp_y)
    
    # can be replaced to do entire columns at same time
    def __model(self) :
        for particle in range(self.numberofparticle) :
            self.__position(particle)
            self.__velocity(particle)
            self.__resetacc(particle)

    def runsim(self) :
        for index in range(self.trialamount) :
            self.__apply_gforce()
            self.__model()
            if (index % self.reportinterval == 0) :
                self.__recordpos()

    def writecsv(self, file : str, particle : int) :
        for index in range(0, len(self.x_list)) :
            x_pos = self.x_list[index][particle]
            y_pos = self.y_list[index][particle]
            print (f"{x_pos}, {y_pos}")
