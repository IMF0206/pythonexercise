a = [1,3,5,7,9]
print a
for i in range(len(a)/2):
	a[i],a[-i-1] = a[-i-1],a[i]
print a