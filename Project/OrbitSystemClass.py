import math
import numpy as np

class OrbitSystem:
    def __init__(self, timeinterval : float, trialamount : int, reportinterval : int):
        # interval - delta t measurement(seconds) amount - number of intervals ran (#) report - number till reporting postition (#)
        self.timeinterval = timeinterval
        self.trialamount = trialamount
        self.reportinterval = reportinterval
        
        self.numberofparticle = 0
        self.dictionary = {}
        self.x_list = []
        self.y_list = []
        self.Grav = 6.6743*(10**-11)

    def addparticle(self, mass : int, x_pos : float, y_pos :float, x_vel : float, y_vel : float):
        self.numberofparticle += 1
        self.dictionary.update({self.numberofparticle : [mass, x_pos, y_pos, x_vel, y_vel, 0, 0]})

    def initalconditions(self) :
        return self.dictionary
    
    # Finds vector for calulations - returns vector pointing from particle 1 to particle 2 - allows direct calculation for gforce components
    def __findvector(self, particle_1, particle_2) :
        x_1 = self.dictionary.get(particle_1)[1]
        x_2 = self.dictionary.get(particle_2)[1]
        y_1 = self.dictionary.get(particle_1)[2]
        y_2 = self.dictionary.get(particle_2)[2]
    
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

    # Force of Gravity of particle_2 on particle_1
    def __gforce(self, particle_1 : int, particle_2 : int) :
        vector = self.__findvector(self, particle_1, particle_2)
        m_2 = self.dictionary.get(particle_2)[0]
        acceleration = self.Grav*m_2/(vector[0])**2
        self.dictionary.get(particle_1)[5] += acceleration*math.cos(vector[1])
        self.dictionary.get(particle_1)[6] += acceleration*math.sin(vector[1])

    #iterates through every particle and applys gforce function
    def __apply_gforce(self) :
        for x in range(0,self.numberofparticle):
            for y in range (0,self.numberofparticle):
                if x != y:
                    self.__gforce(self.dictionary, x, y)

    def __position(self, index : int) :
        x_vel = self.dictionary.get(index)[3]
        y_vel = self.dictionary.get(index)[4]
        x_acc = self.dictionary.get(index)[5]
        y_acc = self.dictionary.get(index)[6]
        dt = self.timeinterval

        self.dictionary.get(index)[1] += .5 * x_acc * (dt ** 2) + x_vel * dt 
        self.dictionary.get(index)[2] += .5 * y_acc * (dt ** 2) + y_vel * dt

    def __velocity(self, index : int) :
        x_acc = self.dictionary.get(index)[5]
        y_acc = self.dictionary.get(index)[6]
        dt = self.timeinterval

        self.dictionary.get(index)[3] += x_acc * dt
        self.dictionary.get(index)[4] += y_acc * dt

    def __resetacc(self, index : int) :
        self.dictionary.get(index)[5] = 0
        self.dictionary.get(index)[6] = 0

    def __recordpos(self) :
        temp_x = []
        temp_y = []

        for index in self.dictionary :
            temp_x.append(self.dictionary.get(index)[1])
            temp_y.append(self.dictionary.get(index)[2])
        
        self.x_list.append(temp_x)
        self.y_list.append(temp_y)
    
    def __model(self) :
        for index in self.dictionary :
            self.__position(index)
            self.__velocity(index)
            self.__resetacc(index)
        
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