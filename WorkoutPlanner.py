# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 10:52:54 2018

@author: trist
"""

import random



#muscle groups
chest = []
back = []
shoulders = []

masterList = []	#unsorted list of all exercises. should be imported from the user's profile

#add string compare to see if the user meant to type the name of an already present exercise or variation, though spelt it wrong
#change to tree structure
def alreadyPresent(exerciseAP):
	for i in range(len(masterList)):
		if masterList[i] == exerciseAP:
			return 1
	return 0

def addExercise(groupAE,exerciseAE,variationsAE):
	if alreadyPresent(exerciseAE) == 0:
		groupAE.append([exerciseAE,variationsAE,-1])
		masterList.append(exerciseAE)
		return 1
	else:
		print('---exercise already present')
	return 0

def addVar(groupAV,exerciseAV,varAV):	#1: variation added		0: exercise does not exist
	for i in range(len(groupAV)):
		if groupAV[i][0] == exerciseAV:
			if groupAV[i][1] == None:
				groupAV[i][1] = [exerciseAV,varAV]
			else:
				groupAV[i][1].append(varAV)
			masterList.append(varAV)
			return 1
	print('---the exercise you are trying to vary is not present')
	return 0
	
addExercise(back,'rows',['bent-over rows','one-arm rows'])
addExercise(back,'pullups',['narrow grip pullups','wide grip pullups'])
addExercise(back,'chinups',None)
addExercise(back,'chest-supported rows',None)
addExercise(back,'shrugs',None)

#user input to generate exercises
#user adds an exercise or an exercise variation
	#for example, looks at list of back workouts and notices that one-arm chinups are not present
	#they add a variation of chinups: one-arm chinups
	#since chinups do not have any variations, two variations are created. chinups and one-arm chinups. one-arm chinups are added to the masterlist


#function "add variation"
	#when adding variation, copy initial exercise as a variation
#function "add exercise"
	#check to see if exercise already exists, either as an exercise or a variation
#function "view all exercises"





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
#reset to 0 before creating a new routine
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

for i in range(6):
	exercise = randomExercise(back)
	if exercise == 0:
		break
	print(exercise)

#return list of exercises (with characteristics) and allow user input
    # reps|sets|weight|up/hold/down|notes
#option to regenerate a single exercise
    #"all exercises checked" and reset factor
#option to add an exercise from the list