
# WRITTEN BY: Chris W Anglin

import random

# Cube CLASS DEFINITION
class Cube():
   
    # CONSTRUCTOR FOR Cube CLASS
    def __init__(self, scrambled=False):
    
        # INITIALIZE ALL SIDES
        self.front = [["FA5F4C", "FA5F4C", "FA5F4C"], ["FA5F4C", "FA5F4C", "FA5F4C"], ["FA5F4C", "FA5F4C", "FA5F4C"]]
        self.top = [["FFCC32", "FFCC32", "FFCC32"], ["FFCC32", "FFCC32", "FFCC32"], ["FFCC32", "FFCC32", "FFCC32"]]
        self.bottom = [["FFF1F3", "FFF1F3", "FFF1F3"], ["FFF1F3", "FFF1F3", "FFF1F3"], ["FFF1F3", "FFF1F3", "FFF1F3"]]
        self.left = [["82B4FF", "82B4FF", "82B4FF"], ["82B4FF", "82B4FF", "82B4FF"], ["82B4FF", "82B4FF", "82B4FF"]]
        self.right = [["7FE0B3", "7FE0B3", "7FE0B3"], ["7FE0B3", "7FE0B3", "7FE0B3"], ["7FE0B3", "7FE0B3", "7FE0B3"]]
        self.back = [["9D99E4", "9D99E4", "9D99E4"], ["9D99E4", "9D99E4", "9D99E4"], ["9D99E4", "9D99E4", "9D99E4"]]

        # OPTION TO SCRAMBLE CUBE UPON CREATION
        if (scrambled == True):
            self.scramble()
    
    # RESET CUBE
    def reset(self):
        self.front = [["FA5F4C", "FA5F4C", "FA5F4C"], ["FA5F4C", "FA5F4C", "FA5F4C"], ["FA5F4C", "FA5F4C", "FA5F4C"]]
        self.top = [["FFCC32", "FFCC32", "FFCC32"], ["FFCC32", "FFCC32", "FFCC32"], ["FFCC32", "FFCC32", "FFCC32"]]
        self.bottom = [["FFF1F3", "FFF1F3", "FFF1F3"], ["FFF1F3", "FFF1F3", "FFF1F3"], ["FFF1F3", "FFF1F3", "FFF1F3"]]
        self.left = [["82B4FF", "82B4FF", "82B4FF"], ["82B4FF", "82B4FF", "82B4FF"], ["82B4FF", "82B4FF", "82B4FF"]]
        self.right = [["7FE0B3", "7FE0B3", "7FE0B3"], ["7FE0B3", "7FE0B3", "7FE0B3"], ["7FE0B3", "7FE0B3", "7FE0B3"]]
        self.back = [["9D99E4", "9D99E4", "9D99E4"], ["9D99E4", "9D99E4", "9D99E4"], ["9D99E4", "9D99E4", "9D99E4"]]

    # CLOCKWISE 'RIGHT' MOVE
    def R(self):
        temp = [self.front[0][2], self.front[1][2], self.front[2][2]]
        self.front[0][2] = self.bottom[0][2]
        self.front[1][2] = self.bottom[1][2]
        self.front[2][2] = self.bottom[2][2]
        self.bottom[0][2] = self.back[0][0]
        self.bottom[1][2] = self.back[1][0]
        self.bottom[2][2] = self.back[2][0]
        self.back[0][0] = self.top[0][2]
        self.back[1][0] = self.top[1][2]
        self.back[2][0] = self.top[2][2]
        self.top[0][2] = temp[0]
        self.top[1][2] = temp[1]
        self.top[2][2] = temp[2]
        temp = self.right[0][0]
        self.right[0][0] = self.right[2][0]
        self.right[2][0] = self.right[2][2]
        self.right[2][2] = self.right[0][2]
        self.right[0][2] = temp
        temp = self.right[0][1]
        self.right[0][1] = self.right[1][0]
        self.right[1][0] = self.right[2][1]
        self.right[2][1] = self.right[1][2]
        self.right[1][2] = temp

    # COUNTER-CLOCKWISE 'RIGHT' MOVE
    def Ri(self):     
        self.R()
        self.R()
        self.R()

    # CLOCKWISE 'UP' MOVE
    def U(self):
        temp = [self.front[0][0], self.front[0][1], self.front[0][2]]
        self.front[0][0] = self.right[0][0]
        self.front[0][1] = self.right[0][1]
        self.front[0][2] = self.right[0][2]
        self.right[0][0] = self.back[0][0]
        self.right[0][1] = self.back[0][1]
        self.right[0][2] = self.back[0][2]
        self.back[0][0] = self.left[0][0]
        self.back[0][1] = self.left[0][1]
        self.back[0][2] = self.left[0][2]
        self.left[0][0] = temp[0]
        self.left[0][1] = temp[1]
        self.left[0][2] = temp[2]
        temp = self.top[0][0]
        self.top[0][0] = self.top[2][0]
        self.top[2][0] = self.top[2][2]
        self.top[2][2] = self.top[0][2]
        self.top[0][2] = temp
        temp = self.top[0][1]
        self.top[0][1] = self.top[1][0]
        self.top[1][0] = self.top[2][1]
        self.top[2][1] = self.top[1][2]
        self.top[1][2] = temp

    # COUNTER-CLOCKWISE 'UP' MOVE
    def Ui(self):       
        self.U()
        self.U()
        self.U()

    # CLOCKWISE 'LEFT' MOVE
    def L(self):
        temp = [self.front[0][0], self.front[1][0], self.front[2][0]]
        self.front[0][0] = self.top[0][0]
        self.front[1][0] = self.top[1][0]
        self.front[2][0] = self.top[2][0]
        self.top[0][0] = self.back[0][2]
        self.top[1][0] = self.back[1][2]
        self.top[2][0] = self.back[2][2]
        self.back[0][2] = self.bottom[0][0]
        self.back[1][2] = self.bottom[1][0]
        self.back[2][2] = self.bottom[2][0]
        self.bottom[0][0] = temp[0]
        self.bottom[1][0] = temp[1]
        self.bottom[2][0] = temp[2]
        temp = self.left[0][0]
        self.left[0][0] = self.left[2][0]
        self.left[2][0] = self.left[2][2]
        self.left[2][2] = self.left[0][2]
        self.left[0][2] = temp
        temp = self.left[0][1]
        self.left[0][1] = self.left[1][0]
        self.left[1][0] = self.left[2][1]
        self.left[2][1] = self.left[1][2]
        self.left[1][2] = temp
    
    # COUNTER-CLOCKWISE 'LEFT' MOVE
    def Li(self):   
        self.L()
        self.L()
        self.L()
    
    # CLOCKWISE 'FRONT' MOVE
    def F(self):     
        temp = [self.top[2][0], self.top[2][1], self.top[2][2]]
        self.top[2][2] = self.left[0][2]
        self.top[2][1] = self.left[1][2]
        self.top[2][0] = self.left[2][2]
        self.left[0][2] = self.bottom[0][0]
        self.left[1][2] = self.bottom[0][1]
        self.left[2][2] = self.bottom[0][2]
        self.bottom[0][0] = self.right[2][0]
        self.bottom[0][1] = self.right[1][0]
        self.bottom[0][2] = self.right[0][0]
        self.right[0][0] = temp[0]
        self.right[1][0] = temp[1]
        self.right[2][0] = temp[2]
        temp = self.front[0][0]
        self.front[0][0] = self.front[2][0]
        self.front[2][0] = self.front[2][2]
        self.front[2][2] = self.front[0][2]
        self.front[0][2] = temp
        temp = self.front[0][1]
        self.front[0][1] = self.front[1][0]
        self.front[1][0] = self.front[2][1]
        self.front[2][1] = self.front[1][2]
        self.front[1][2] = temp

    # COUNTER-CLOCKWISE 'FRONT' MOVE
    def Fi(self):      
        self.F()
        self.F()
        self.F()

    # CLOCKWISE 'BOTTOM' MOVE
    def D(self):     
        temp = [self.front[2][0], self.front[2][1], self.front[2][2]]
        self.front[2][0] = self.left[2][0]
        self.front[2][1] = self.left[2][1]
        self.front[2][2] = self.left[2][2]
        self.left[2][0] = self.back[2][0]
        self.left[2][1] = self.back[2][1]
        self.left[2][2] = self.back[2][2]
        self.back[2][0] = self.right[2][0]
        self.back[2][1] = self.right[2][1]
        self.back[2][2] = self.right[2][2]
        self.right[2][0] = temp[0]
        self.right[2][1] = temp[1]
        self.right[2][2] = temp[2]
        temp = self.bottom[0][0]
        self.bottom[0][0] = self.bottom[2][0]
        self.bottom[2][0] = self.bottom[2][2]
        self.bottom[2][2] = self.bottom[0][2]
        self.bottom[0][2] = temp
        temp = self.bottom[0][1]
        self.bottom[0][1] = self.bottom[1][0]
        self.bottom[1][0] = self.bottom[2][1]
        self.bottom[2][1] = self.bottom[1][2]
        self.bottom[1][2] = temp


    # COUNTER-CLOCKWISE 'BOTTOM' MOVE
    def Di(self):      
        self.D()
        self.D()
        self.D()

    # CLOCKWISE 'BACK' MOVE
    def B(self):     
        temp = [self.top[0][0], self.top[0][1], self.top[0][2]]
        self.top[0][0] = self.right[0][2]
        self.top[0][1] = self.right[1][2]
        self.top[0][2] = self.right[2][2]
        self.right[0][2] = self.bottom[2][2]
        self.right[1][2] = self.bottom[2][1]
        self.right[2][2] = self.bottom[2][0]
        self.bottom[2][0] = self.left[0][0]
        self.bottom[2][1] = self.left[1][0]
        self.bottom[2][2] = self.left[2][0]
        self.left[2][0] = temp[0]
        self.left[1][0] = temp[1]
        self.left[0][0] = temp[2]
        temp = self.back[0][0]
        self.back[0][0] = self.back[2][0]
        self.back[2][0] = self.back[2][2]
        self.back[2][2] = self.back[0][2]
        self.back[0][2] = temp
        temp = self.back[0][1]
        self.back[0][1] = self.back[1][0]
        self.back[1][0] = self.back[2][1]
        self.back[2][1] = self.back[1][2]
        self.back[1][2] = temp

    # COUNTER-CLOCKWISE 'BACK' MOVE
    def Bi(self):     
        self.B()
        self.B()
        self.B()

    # SCRAMBLE THE CUBE
    def scramble(self):
        for i in range(1):
            x = random.uniform(0, 1)
            if (x <= 1/12):
                self.R()
            elif (x <= 2/12):
                self.Ri()
            elif (x <= 3/12):
                self.U()
            elif (x <= 4/12):
                self.Ui()
            elif (x <= 5/12):
                self.L()
            elif (x <= 6/12):
                self.Li()
            elif (x <= 7/12):
                self.F()
            elif (x <= 8/12):
                self.Fi()
            elif (x <= 9/12):
                self.D()
            elif (x <= 10/12):
                self.Di()
            elif (x <= 11/12):
                self.B()
            else:
                self.Bi()