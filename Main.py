#Reach to the top
from Game_Objects import *
from graphics import *
from Obstacles_Control import *
def main():
    
    Power="On"
    a=0
    b=0
    while Power == "On":
      while b==0:
        print("REACHING THE TOP (THE GAME)")
        print("\nHi, Welcome to Reaching the Top")
        print("Select which action you would like to do:\n")
        print("Play - Press 1")
        print("Instructions of the Game - press 2")
        print("Quit - press 0")
        while a == 0:
         try:
           Input=int(input("Insert your Option: "))
           a=1
         except:
           print("Please enter a number not a word.")
         
        if Input == 1:
           GOB=Game_Object() 
           Game=Obstacle_Control()
           GOB.setWalls_and_Ball()
           while Game.GO == 0:
         
              Game.Ball_Movement(GOB)
              Game.Game_Time(GOB)
              Name,FSC=Game.Over(GOB)
              
           print("\n\n\nName: ",Name,"\nFinal Score: ",FSC,"\n\n",)
           PowerD=input("Do you want to exit game: ")
           
           if PowerD == "Yes" or PowerD=="yes" or PowerD == "Y" or PowerD == "y":
             print("Good bye")
             GOB.Screen.close()
             Power ="Off"
             b=1
           else:
            Power="On"
            b=0
            a=0
            GOB.Screen.close()
        elif Input == 2:
          File=open("README.md","r")
          print(File.read())
          File.close()
          PowerD=input("Do you want to exit game: ")
          if PowerD == "Yes" or PowerD=="yes" or PowerD == "Y" or PowerD == "y":
             print("Good bye")
             Power ="Off"
             b=1
          else:
            Power="On"
            a=0
            b=0
        elif Input == 0:
          print("Good bye")
          Power ="Off"
          b=1
        else:
          print("Value not permited, enter a value that refers to an action:")
          Input=int(input("Insert your Option: "))
          
          

main()
