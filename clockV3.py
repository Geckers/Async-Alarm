import asyncio
import time
import aioconsole

def getTime()-> list:
    #using local time because that makes more sense to me
    clock= time.localtime()
    currentTime= clock[3:6]
    #converts time into usable list that ignores year month day ex...
    return currentTime
def timeToSecs(currentTime):
    trueTime=int(currentTime[0])*3600 +int(currentTime[1])*60 + int(currentTime[2])
    return trueTime

async def Interval(name: str="",timeWanted: list= (0,0,0))-> None:
	print(f"alarm {name} created")
	while True:
		await asyncio.sleep(timeToSecs(timeWanted))
		print (f"Ring #{name}")
	await asyncio.sleep(1)
async def Single(name: str="",timeWanted:list= (0,0,0))->None:
	print(f"alarm {name} created")
	while True:
		currentTime=getTime()
		if timeToSecs(currentTime)==timeToSecs(timeWanted):
			print (f"Ring #{name}")
		await asyncio.sleep(1)

async def main()->None:
	startTime=getTime()
	print(f"current time is {startTime[0]}:{startTime[1]}:{startTime[2]}")
	userInput=""
	todo={}
	todoname=0
	try:
		done,_pending=await asyncio.wait(todo.values(),timeout=1)
	except ValueError:
		print("no alarms")
	while userInput!="terminate":
		try:
			print(f"current alarms created {len(todo.values())}")
		except:
			print("need input")
		userInput=await aioconsole.ainput()
		if userInput=="terminate":
			print('terminating')
			quit()
		userInput=userInput.split()
		try:
			if userInput[0]=="once":
				todoname=todoname+1
				userTime=userInput[1]
				task=asyncio.create_task(Single(todoname,userTime.split(":")))
				todo[todoname]=task
			elif userInput[0]=="interval":
				todoname=todoname+1
				userTime=userInput[1]
				task=asyncio.create_task(Interval(todoname,userTime.split(":")))
				todo[todoname]=task
			elif userInput[0]=="cancel":
				try:
					todo[int(userInput[1])].cancel()
					del todo[int(userInput[1])]
				except:
					print(f"no alarm with name {int(userInput[1])} exists")
		except:
			print("please type in correct phrase:")

asyncio.run(main())

#### In order to use code use one of 4 diffrent commands interval, once,terminate, cancel
### for interval and once please type either interval or once then ##:##:## please use integers and the 24 hour time system (6pm is written as 18:00:00)
### terminate just cancels the entire program
### in order to cancel remeber which ID your timer has, the Id starts at 1 and increases as more are created. The first timer you write will be timer 1 and to cancel simply write cancel 1
