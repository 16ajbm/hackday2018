# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 10:52:54 2018

@author: trist
"""

import random

#using lists


#lists of exercises
#        [exercise],[[var1],[var2]]
chest = []
back = []
shoulders = []

def addExercise(groupAE,exerciseAE,variationsAE):
    groupAE.append([exerciseAE,variationsAE,-1])

addExercise(back,'rows',['bent-over rows','one-arm rows'])
addExercise(back,'pullups',['narrow grip pullups','wide grip pullups'])
addExercise(back,'chinups',None)
addExercise(back,'chest-supported rows',None)
addExercise(back,'shrugs',None)





#given muscle group, point to a list of exercises
#randomly choose n exercises (or variations)
random.seed()

def checkIfUsed(groupCIU,indexCIU,countCIU):
	if groupCIU[indexCIU][2] == -1:
		return indexCIU
	elif countCIU > 10:
		print('---no available workouts')
		return -1
	else:
		indexCIU += 1
		indexCIU = indexCIU%len(groupCIU)
		indexCIU = checkIfUsed(groupCIU,indexCIU,countCIU+1)
		return indexCIU

def randomExercise(groupRE):
#random exercise
	index = random.randint(0,len(groupRE)-1)
#check if exercise is already used
	index = checkIfUsed(groupRE,index,0)
	if index == -1:	#error check
		return 0
#assign exercise
	exercise = groupRE[index]
	groupRE[index][2] = 0
#assign variation (if applicable)
	if exercise[1] != None:
		index = random.randint(0,len(exercise[1])-1)
		exercise = exercise[1][index]
	else:
		exercise = exercise[0]

	return exercise

<<<<<<< HEAD
def randomExercise():
    index = random.randint(0,len(back)-1)
    print(f'precheck:{back[index]}')
    index = checkIfUsed(back,index,0)
    print(f'postcheck:{back[index]}')
    exercise = back[index]
    back[2] = -1
    if exercise[1] != None:
        index = random.randint(0,len(exercise[1])-1)
        exercise = exercise[1][index]
        print(f'variation:{back[index]}')

for i in range(5):
	randomExercise()
=======
for i in range(6):
	exercise = randomExercise(back)
	if exercise == 0:
		break
	print(exercise)
>>>>>>> ab254e78f5a70038d2c753d0e7bc0110dec74d01

#print(f'exercise: {back[index]}')

#make sure the same exercise doesn't get chosen twice (factor in list, reset)

#check which exercises have been done by user in the past, show previous stats


#return list of exercises (with characteristics) and allow user input
    # reps|sets|weight|up/hold/down|notes
#option to regenerate a single exercise
    #"all exercises checked" and reset factor
