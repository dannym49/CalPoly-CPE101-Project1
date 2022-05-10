from math import *
   
def poundsToKG(pounds):
   kilograms = float((pounds * 0.453592))
   return kilograms

# object will be a one character string, for example: 't'
def getMassObject(massOb):
   
   t = 0.1
   p = 1.0
   r = 3.0
   g = 5.3
   l = 9.07
   if massOb == 't':
      massOb = 0.1
   elif massOb == 'p':
      massOb = 1.0
   elif massOb == 'r':
      massOb = 3.0
   elif massOb == 'g':
      massOb = 5.3
   elif massOb == 'l':
      massOb = 9.07
   else:
      massOb = 0.0

   return massOb
   
def getVelocityObject(distance):
   gravity = 9.8
   velocityObject = sqrt(gravity*distance/2)
   return velocityObject

def getVelocitySkater(massSkater, massObject, velObject):
   velocitySkater = (massObject * velObject / massSkater)
   return velocitySkater

