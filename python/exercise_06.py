#fibonacci
def fib(n):
	if(n==1):
		return [1]
	elif(n==2):
		return [1,1]
	else:
		f = [1,1]
		for i in range(2,n):
			f.append(f[-1]+f[-2])
		return f
print fib(10)