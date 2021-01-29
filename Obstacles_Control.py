#Timer and Score objects
from graphics import *

class Obstacle_Control:
    def __init__(self):
      self.S=50
      self.Scob=0
      self.Tap=0
      self.TrS=10000000000
      self.Score=0
      self.GO=0
      self.Ch=0
      self.Lst_Plc=Point(0,0)
      self.Balling=Circle(Point(100,100),15)

    def Ball_Movement(self,GOB):
       
        
         Center=GOB.Screen.checkMouse()
      
      
         if Center != GOB.Ball.getCenter() and self.Ch == 0 and Center != None:
           self.TrS=100000
           GOB.Ball.undraw()
           self.Balling=Circle(Center,10)
           self.Lst_Plc=Center
           self.Balling.setFill("red")
           self.Balling.setOutline("red")
           self.Balling.draw(GOB.Screen)
           self.Ch=1
           self.Score=self.Score+5  #Score Here!!!!!
           self.Scob=self.Scob+25
         elif Center != self.Balling.getCenter() and Center != None and self.Ch == 1:
           self.Balling.undraw()
           self.Balling=Circle(Center,10)
           self.Balling.setFill("red")
           self.Balling.setOutline("red")
           self.Balling.draw(GOB.Screen)
           self.Score=self.Score+5  #Score Here!!!!!
           self.Scob=self.Scob+25
         else:
          if self.Ch == 1:
            self.Balling.move(0,0)
            self.Scob=self.Scob
            self.Score=self.Score
          else:
            self.Ch=0
            self.Scob=self.Scob
            self.Score=self.Score
            
    def Game_Time(self,GOB):   
       if self.TrS <= 0:
        self.TrS=100000
        if (GOB.Wall[0].getP2()).getY()< 0:
          GOB.Wall[0].move(0, 500-(GOB.Wall[0].getP2()).getY()) 
        else:
          GOB.Wall[0].move(0,-3)
          self.Balling.move(0,-3)
        if (GOB.Wall[1].getP2()).getY()< 0:
          GOB.Wall[1].move(0, 500-(GOB.Wall[1].getP2()).getY())  
        else:
          GOB.Wall[1].move(0,-3)
        if (GOB.Wall[2].getP2()).getY()< 0:
          GOB.Wall[2].move(0, 500-(GOB.Wall[2].getP2()).getY())
        else:
          GOB.Wall[2].move(0,-3)
        if (GOB.Wall2[0].getP2()).getY()< 0:
          GOB.Wall2[0].move(0, 500-(GOB.Wall2[0].getP2()).getY())  
        else:
          GOB.Wall2[0].move(0,-3)
          
        if (GOB.Wall2[1].getP2()).getY()< 0:
          GOB.Wall2[1].move(0, 500-(GOB.Wall2[1].getP2()).getY())  
        else:
          GOB.Wall2[1].move(0,-3)
          
        if (GOB.Wall2[2].getP2()).getY()< 0:
          GOB.Wall2[2].move(0, 500-(GOB.Wall2[2].getP2()).getY())
        else:
          GOB.Wall2[2].move(0,-3)    
       else:  
         if self.Scob == 50:
             self.Scob=0
             self.S=self.S+50
             self.TrS=self.TrS-self.S
         else:
            self.TrS=self.TrS-self.S
      
    def Over(self,GOB):
         
         
      if (self.Balling.getCenter()).getY()<=0:
        self.GO=1,
        Final_Score=int(self.Score)
        Name=input("Enter name or nickname: ")
        return Final_Score,Name
      else:
        self.GO=0
        return 0,"None"
     

if __name__ =="__Obstacle_Control__":

  Obstacle_Control()

