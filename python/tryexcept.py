num = input("enter the user value:")
try:
	val = int(num)
	print("Conversion successful")
except:
	val = -1
if val > 0: 
	print("its a number:", num)
else:
	print("not a num")