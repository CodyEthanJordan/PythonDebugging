# Cody Jordan
# Homework 7

import numpy as np

# Problem 1
print('Problem 1')


def garden(length, carrot=0, lettuce=0, pepper=0, tomato=0):
    '''garden takes the length of my garden in feet and the desired yeild in pounds
    returns a tuple indicating
    -is this garden posible?
    -total required length
    -number of each plant required'''

    #first column is plants needed, second is feet needed
    gardenRows = np.array([requiredSpace('carrot', carrot),
                           requiredSpace('lettuce', lettuce),
                           requiredSpace('pepper', pepper),
                           requiredSpace('tomato', tomato),
                           ])

    feetNeeded = np.max(gardenRows[:,1])
    willFit = feetNeeded < length    
        
    return (willFit, feetNeeded, *gardenRows[:,1]) #Mock output

def requiredSpace(plantName, poundsDesired):
    '''Figures out how long the row needs to be, and number of plants needed.
       Returns a tuple of required length in feet, and number of plants'''
     
    requiredFeet = {'carrot'  : 0.25,
                    'lettuce' : 1.5,
                    'pepper'  : 2.0,
                    'tomato'  : 2.0}
                    
    poundsProduced = {'carrot'  : 0.5,
                      'lettuce' : 1.0,
                      'pepper'  : 2.0,
                      'tomato'  : 10.0}
    
    plantsNeeded = np.ceil(poundsDesired / poundsProduced[plantName])
    feetNeeded = plantsNeeded * requiredFeet[plantName]
    
    return plantsNeeded, feetNeeded
             
def gardenreport(possible, length, carrot, lettuce, pepper, tomato):
    '''Produces a reprot based on the output of garden'''
    if possible:
        print("Your garden plan works!")
    else:
        print("Your garden is IMPOSSIBLE!")
        
    print("Row Length: " + str(length))
    print("Plants to plant")
    print("---------------")
    print("  Carrots:" + str(carrot))
    print("  Lettuce:" + str(lettuce))
    print("  Peppers:" + str(pepper))
    print("  Tomatoes:" + str(tomato))
    print("") #blank line at the end
    return
    
problem1Garden = garden(12, carrot=40, lettuce=2, pepper=6, tomato=3)
print(problem1Garden)

#output report both ways
gardenreport(*problem1Garden)

gardenreport(*garden(12, carrot=40, lettuce=2, pepper=6, tomato=3))