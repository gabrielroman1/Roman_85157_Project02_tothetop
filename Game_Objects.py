#Reach to the Top (Objects)


from graphics import *

def Game_Object():
  """ Here are all the objects made for the use of the game:
      - the jumping ball
      - the Walls.
      - Maybe others will come
  """
  #Screen
  Screen = GraphWin("Reaching the Top", 500, 500)
  Screen.setCoords(0,0,500,500)
  Screen.setBackground("black")

  #Ball
  Center= Point(10,15)
  Ball=Circle(Center,10)
  Ball.setFill('red')
  Ball.setOutline("red")
  #Ball.draw(Screen)
  
  
  #Walls
  #LEFT WALL
  Wall_L=Rectangle(Point(0,0),Point(100,5))
  Wall_L.setFill("white")
  #Wall_L.draw(Screen)
  #CENTER WALL
  Wall_C=Rectangle(Point(175,0),Point(325,5))
  Wall_C.setFill("white")
  #Wall_C.draw(Screen)
  #RIGHT WALL
  Wall_R=Rectangle(Point(400,0),Point(500,5))
  Wall_R.setFill("white")
  #Wall_R.draw(Screen)
  Wall=[Wall_L,Wall_C,Wall_R]

  #Wait=Screen.getMouse()
  #Screen.close()
  #I need to create another function and change the condition to that function
  #with the things that are comented it would be test. 
  return Screen,Ball,Wall
  
if __name__=='__Game_Object__':

  Game_Object()
