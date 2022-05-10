#Project 1
#
# Name: Danny Moreno
# Instructor: Workman
# Section: 13


from math import *
from funcs import *

def main():
   weight = float(input("How much do you weigh (pounds)? " ))
   personMass = poundsToKG(weight)
   distance = float(input("How far away is your professor (meters)? "))
   objVel = getVelocityObject(distance) 
   massOb = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")
   objectMass = getMassObject(massOb)
   skaterVel = (objectMass* objVel / personMass)

   if objectMass <= 0.1:
      print("\nNice throw! You're going to get an F!")
   elif 0.1< objectMass <=1.0:
      print("\nNice throw! Make sure your professor is OK.")
   elif objectMass > 1.0 and distance < 20:
      print("\nNice throw! How far away is the hospital?")
   elif objectMass > 1.0 and distance >= 20:
      print("\nNice throw! RIP professor.")

   print("Velocity of skater: %.3f" % skaterVel , "m/s")

   if skaterVel < 0.2:
      print("My grandmother skates faster than you!")
   elif skaterVel >= 1.0:
      print("Look out for that railing!!!")



  
  

if __name__ == '__main__':
   main()
