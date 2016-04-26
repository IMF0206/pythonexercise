#use {} dictionary
import time

myId = {1:'a',2:'b'}
for key,value in dict.items(myId):
	time.sleep(1)
	print key,value