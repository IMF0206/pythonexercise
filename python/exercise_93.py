import time
start = time.clock()
for i in range(10000):
	print i,
end = time.clock()
print '%6.3f' %(end - start)