#Timer and Score objects
from graphics import *

class Obstacle_Control:
    """ This class containts all the control algorithm
        the constructor to set all the parameters of control of the game,
        the update of the game and time, the score and the conditions. Finally,
        the restrictions and the reason for game over. 
    """
    def __init__(self):
      """ Here we have the parameters set for the game, control variables,score
         and time.
      """
      self.S=50
      self.Scob=0
      self.Tap=0
      self.TrS=10000000000
      self.Score=0
      self.GO=0
      self.Ch=0
      self.Lst_Plc=Point(0,0)
      self.Balling=Circle(Point(100,100),15)
      self.Wallnum=11
      self.Next=2

    def Ball_Movement(self,GOB):
         """ This method is for controlling the ball on moving where it needs to
            from starting the game to moving through the game. Also, yo can see
            that this function is the one that gives the score. Other methods mentioned
            here, are describe in their respective places.
         """
        
         Center=GOB.Screen.checkMouse()
          
      
         if Center != GOB.Ball.getCenter() and self.Ch == 0 and Center != None:
           Condition=self.Clicked(Center,GOB)
           print
           if not(Condition):
              self.TrS=100000
              
           else:
             self.TrS=100000
             GOB.Ball.undraw()
             self.Balling=Circle(self.Centering(Center,GOB),10)
             self.Lst_Plc=Center
             self.Balling.setFill("red")
             self.Balling.setOutline("red")
             self.Balling.draw(GOB.Screen)
             self.Ch=1
             self.Score=self.Score+5  #Score Here!!!!!
             self.Scob=self.Scob+25
         elif Center != self.Balling.getCenter() and Center != None and self.Ch == 1:
            Condition=self.Clicked(Center,GOB)
            if not(Condition):
              self.Scob=self.Scob
              self.Score=self.Score
            else:
              self.Balling.undraw()
              self.Balling=Circle(self.Centering(Center,GOB),10)
              self.Balling.setFill("red")
              self.Balling.setOutline("red")
              self.Balling.draw(GOB.Screen)
              self.Score=self.Score+5  #Score Here!!!!!
              self.Scob=self.Scob+25
         else:
          if self.Ch == 1:
            self.Balling.move(0,0)
          else:
            self.Ch=0
            self.TrS=100000


            
    def Clicked(self,Center,GOB):
        """ This method is for restraining the selection of the ball where it should be
            if you select wrong it wont move the ball. If you select of the floor, it wont move the ball.
            if you select another latter that isnt the correct one, then the ball wont move.
        """
        if (GOB.Wall[0].getP1().getX()<= Center.getX() and GOB.Wall[0].getP2().getX()>= Center.getX())and(GOB.Wall[0].getP1().getY()< Center.getY() and GOB.Wall[0].getP2().getY()+15 >= Center.getY())and self.Next==1:
            self.Wallnum=11
            self.Next=2
            
            return True
        elif (GOB.Wall[1].getP1().getX()<= Center.getX() and GOB.Wall[1].getP2().getX()>= Center.getX())and(GOB.Wall[1].getP1().getY()< Center.getY() and GOB.Wall[1].getP2().getY()+15 >= Center.getY())and self.Next==2:
            self.Wallnum=12
            self.Next=3
            
            return True
        elif (GOB.Wall[2].getP1().getX()<= Center.getX() and GOB.Wall[2].getP2().getX()>= Center.getX())and(GOB.Wall[2].getP1().getY()< Center.getY() and GOB.Wall[2].getP2().getY()+15 >= Center.getY())and self.Next==3:
            self.Wallnum=13
            self.Next=5
            
            return True
        elif (GOB.Wall2[0].getP1().getX()<= Center.getX() and GOB.Wall2[0].getP2().getX()>= Center.getX())and(GOB.Wall2[0].getP1().getY()< Center.getY() and GOB.Wall2[0].getP2().getY()+15 >= Center.getY())and self.Next==4:
            self.Wallnum=21
            self.Next=6
            
            return True
        elif (GOB.Wall2[1].getP1().getX()<= Center.getX() and GOB.Wall2[1].getP2().getX()>= Center.getX())and(GOB.Wall2[1].getP1().getY()< Center.getY() and GOB.Wall2[1].getP2().getY()+15 >= Center.getY())and self.Next==5:
            self.Wallnum=22
            self.Next=4
            
            return True
        elif (GOB.Wall2[2].getP1().getX()<= Center.getX() and GOB.Wall2[2].getP2().getX()>= Center.getX())and(GOB.Wall2[2].getP1().getY()< Center.getY() and GOB.Wall2[2].getP2().getY()+15 >= Center.getY())and self.Next==6:
            self.Wallnum=23
            self.Next=1
            
            return True
        else:
            
            return False

        
        
    def Centering(self,Center,GOB):
         """This function centers the correct selection you made on the corresponding floor.
         """
         if self.Wallnum==11:
            RecCenter=GOB.Wall[0].getCenter()
            Center=Point(RecCenter.getX(),(RecCenter.getY()+10))
            
            return Center
         elif self.Wallnum==12:
            RecCenter=GOB.Wall[1].getCenter()
            Center=Point(RecCenter.getX(),(RecCenter.getY()+10))
            
            return Center
         elif self.Wallnum==13:
            RecCenter=GOB.Wall[2].getCenter()
            Center=Point(RecCenter.getX(),(RecCenter.getY()+10))
            
            return Center
         elif self.Wallnum==21:
            RecCenter=GOB.Wall2[0].getCenter()
            Center=Point(RecCenter.getX(),(RecCenter.getY()+10))
            
            return Center
         elif self.Wallnum==22:
            RecCenter=GOB.Wall2[1].getCenter()
            Center=Point(RecCenter.getX(),(RecCenter.getY()+10))
            
            return Center
         elif self.Wallnum==23:
            RecCenter=GOB.Wall2[2].getCenter()
            Center=Point(RecCenter.getX(),(RecCenter.getY()+10))
            
            return Center
         else:
            
            return Center
        
        
            
    def Game_Time(self,GOB):
       """ This method controls the time, the score, game dificulty and the walls movement.
       """
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
      """ This function gives the reason for game over, when it reaches the ground, then is game over
           It will return the final score and ask for your name to print it all together. 
      """
         
      if (self.Balling.getCenter()).getY()<=0:
        self.GO=1,
        Final_Score=int(self.Score)
        Name=input("Enter name or nickname: ")
        return Final_Score,Name
      else:
        self.GO=0
        return 0,"None"
     

if __name__ =="__Obstacle_Control__":

  OC=Obstacle_Control()

