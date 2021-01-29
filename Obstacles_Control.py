#Timer and Score objects
from graphics import *
def Obstacle_Control(Screen,Ball,Wall): 
    S=50
    Scob=0
    Tap=0
    TrS=10000000000
    Score=0
    GO=0
    Ch=0
    Lst_Plc=Point(0,0)
    Balling=Circle(Point(100,100),15)
    Wall[0].draw(Screen)
    Wall[1].move(0,75)
    Wall[1].draw(Screen)
    Wall[2].move(0,150)
    Wall[2].draw(Screen)
    Wall2=[]
    Wall2.append(Wall[0].clone())
    Wall2.append(Wall[1].clone())
    Wall2.append(Wall[2].clone())
    Wall2[0].move(0,350)
    Wall2[0].draw(Screen)
    Wall2[1].move(0,175)
    Wall2[1].draw(Screen)
    Wall2[2].move(0,300)
    Wall2[2].draw(Screen)
    Ball.draw(Screen)
    while GO == 0:
        
      Center=Screen.checkMouse()
      
      
      if Center != Ball.getCenter() and Ch == 0 and Center != None:
         TrS=100000
         Ball.undraw()
         Balling=Circle(Center,10)
         Lst_Plc=Center
         Balling.setFill("red")
         Balling.setOutline("red")
         Balling.draw(Screen)
         Ch=1
         Score=Score+5  #Score Here!!!!!
         Scob=Scob+25
      elif Center != Balling.getCenter() and Center != None and Ch == 1:
         Balling.undraw()
         Balling=Circle(Center,10)
         Balling.setFill("red")
         Balling.setOutline("red")
         Balling.draw(Screen)
         Score=Score+5  #Score Here!!!!!
         Scob=Scob+25
      else:
        if Ch == 1:
          Balling.move(0,0)
          Scob=Scob
          Score=Score
        else:
          Ch=0
          Scob=Scob
          Score=Score
          
      if TrS <= 0:
        TrS=100000
        if (Wall[0].getP2()).getY()< 0:
          Wall[0].move(0, 500-(Wall[0].getP2()).getY()) 
        else:
          Wall[0].move(0,-3)
          Balling.move(0,-3)
        if (Wall[1].getP2()).getY()< 0:
          Wall[1].move(0, 500-(Wall[1].getP2()).getY())  
        else:
          Wall[1].move(0,-3)
        if (Wall[2].getP2()).getY()< 0:
          Wall[2].move(0, 500-(Wall[2].getP2()).getY())
        else:
          Wall[2].move(0,-3)
        if (Wall2[0].getP2()).getY()< 0:
          Wall2[0].move(0, 500-(Wall2[0].getP2()).getY())  
        else:
          Wall2[0].move(0,-3)
          
        if (Wall2[1].getP2()).getY()< 0:
          Wall2[1].move(0, 500-(Wall2[1].getP2()).getY())  
        else:
          Wall2[1].move(0,-3)
          
        if (Wall2[2].getP2()).getY()< 0:
          Wall2[2].move(0, 500-(Wall2[2].getP2()).getY())
        else:
          Wall2[2].move(0,-3)
          
      else:
          
         if Scob == 50:
             Scob=0
             S=S+50
             TrS=TrS-S
         else:
            TrS=TrS-S
      
          
         
      if (Balling.getCenter()).getY()<=0:
         GO=1
      else:
         GO=0
            
    
    Final_Score=int(Score)
    Name=input("Enter name or nickname: ")
     
    return Final_Score,Name

if __name__ =="__Obstacle_Control__":

  Obstacle_Control()

