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
  def setWalls_and_Ball(self):
    self.Wall[0].draw(self.Screen)#1 first left
    self.Wall[1].move(0,65)
    self.Wall[1].draw(self.Screen)#2 first middle
    self.Wall[2].move(0,150)
    self.Wall[2].draw(self.Screen)#3 first right
    self.Wall2[0].move(0,300)
    self.Wall2[0].draw(self.Screen)#5 second left
    self.Wall2[1].move(0,225)
    self.Wall2[1].draw(self.Screen)#4 second middle
    self.Wall2[2].move(0,400)
    self.Wall2[2].draw(self.Screen)#6 second right
    self.Ball.draw(self.Screen)
  #Work with the object conditions, work with the notes in every method. 
if __name__=='__Game_Object__':
  GOB=Game_Object()
  GOB.setWalls_and_Ball()
  
