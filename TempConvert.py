#TempConvert.py
TempStr = input("Temperature:")
if TempStr[-1] in ['F','f']:
	C = (eval(TempStr[0:-1])-32)/1.8
	print("Temperature:{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
	C = 1.8*eval(TempStr[0:-1])+32
	print("Temperature:{:.2f}F".format(C))
else:
	print("Error Temperature")
