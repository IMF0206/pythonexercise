#huiwen panduan
while(True):
	x = raw_input('enter your number: ')
	a = int(x)
	flag = True
	for i in range(len(x)/2):
		if(x[i]!=x[-i-1]):
			flag = False
			break
	if(flag):
		print '%d------>YES' %a
	else:
		print '%d------>NO' %a
