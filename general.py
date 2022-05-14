import time

def waitFunction(timeToWait):
	startTime = time.time()
	while True:
		if time.time() - startTime > timeToWait: # tests if time has surpassed the wait time
			break # exits the while loop

def waitFunction(startTime,timeToWait):
	while True:
		if time.time() - startTime > timeToWait: # tests if time has surpassed the wait time
			break # exits the while loop