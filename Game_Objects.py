#Reach to the Top (Objects)


from graphics import *

class Game_Object:

  def __init__(self):
    
      """ Here are all the objects made for the use of the game:
      - the jumping ball
      - the Walls.
      - Maybe others will come
      """
      #Screen
      self.Screen = GraphWin("Reaching the Top", 500, 500)
      self.Screen.setCoords(0,0,500,500)
      self.Screen.setBackground("black")
      #Ball
      Center= Point(10,15)
      self.Ball=Circle(Center,10)
      self.Ball.setFill('red')
      self.Ball.setOutline("red")
  
  
      #Walls
      #LEFT WALL
      Wall_L=Rectangle(Point(0,0),Point(100,5))
      Wall_L.setFill("white")
      #CENTER WALL
      Wall_C=Rectangle(Point(175,0),Point(325,5))
      Wall_C.setFill("white")
      #RIGHT WALL
      Wall_R=Rectangle(Point(400,0),Point(500,5))
      Wall_R.setFill("white")
      #Wall_R.draw(Screen)
      self.Wall=[Wall_L,Wall_C,Wall_R]
      self.Wall2=[]
      self.Wall2.append(self.Wall[0].clone())
      self.Wall2.append(self.Wall[1].clone())
      self.Wall2.append(self.Wall[2].clone())
  def getScreen(self):
     return self.Screen
  def getBall(self):
     return self.Ball
  def getWalls(self):
     return self.Wall,self.wall2
  def setWalls(self):
    self.Wall[0].draw(self.Screen)
    self.Wall[1].move(0,75)
    self.Wall[1].draw(self.Screen)
    self.Wall[2].move(0,150)
    self.Wall[2].draw(self.Screen)
    self.Wall2[0].move(0,350)
    self.Wall2[0].draw(self.Screen)
    self.Wall2[1].move(0,175)
    self.Wall2[1].draw(self.Screen)
    self.Wall2[2].move(0,300)
    self.Wall2[2].draw(self.Screen)
    self.Ball.draw(self.Screen)
  #Work with the object conditions, work with the notes in every method. 
if __name__=='__Game_Object__':

  Game_Object()
