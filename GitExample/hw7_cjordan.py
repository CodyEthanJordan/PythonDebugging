#!/usr/bin/env python3
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
        
    return (willFit, feetNeeded, *gardenRows[:,1])

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
    
    plantsNeeded = np.floor(poundsDesired / poundsProduced[plantName])
    # floor function?
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


# Problem 2
print('Problem 2')

def mortgage_payment(termYears, apr, initialPrinciple):
    '''Calculates monthly mortage payment under given conditions
    
    Takes in the term in years, the annual percentage in percent form, and the initial amount borrowed
    
    returns the monthly payment based on formula from
    
    http://en.wikipedia.org/wiki/Mortgage_calculator '''
    
    r = apr / 100 / 12
    N = 12 * termYears
    
    return (initialPrinciple * r * (1+r)**N) / ((1+r)**N - 1)
    
print(mortgage_payment(30, 4, 200000))
# Checked this against Google's mortgage calculator, works
    
    