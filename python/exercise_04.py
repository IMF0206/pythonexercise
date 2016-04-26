y = int(raw_input("input year:\n"))
m = int(raw_input('input month:\n'))
d = int(raw_input('input day:\n'))
month = [0,31,59,90,120,151,181,212,243,273,304,334]
sum = month[m]+d;
if(m>12 or m<1):
	print 'error'
elif(y%400==0 or (y%4==0 and y%100!=0)):
	if(m>2):
		sum += 1
		print 'sum:\n %d'%sum
else:
	print 'sum:\n %d'%sum

