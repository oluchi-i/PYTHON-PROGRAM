# ADD HEADER COMMENT HERE
# Purpose: THIS PROGRAM CALCULATES THE TRAJECTORY OF A PROJECTILE.
# Author:  OLUCHI IKWUEGBU
# Date:    10/08/23

# import necessary module
import math

# define the required function below this line
def projectileMotion(theta, speed, distance):
    deg_to_radians = theta * (math.pi/180)          #degrees to radians
    height = (distance * math.tan(deg_to_radians)) -  ((9.81 * math.pow(distance, 2))  / (2 * math.pow(speed, 2) * math.pow(math.cos(deg_to_radians), 2)))
    return height       #return height(y formula)

# main script
if __name__ == "__main__" :
    # main script code goes below this line. Keep the same indentation level as this line.
    theta = int(input("Enter launch angle in degrees: "))
    speed = int(input("Enter launch velocity in meters per seconds: "))     #user input
    distance = int(input("Enter distance in meters: "))
    y = projectileMotion(theta, speed, distance)        #function call
    print("The height of this projectile at a distance of",distance, "meters along its trajectory is", (f'{y:.2f}'), "meters")      #answer in 2 d.p.
    