count = 0 
sum = 0
while True:
	n = ("enter thr number:")
	if n == 'exit':
		break
	try:
		fval = float(n)
	except:
		print("invalid input")
		continue
    count = count + 1
    sum = sum + fval

print("TOTAL",count)
print("Sum",sum)
print("Average",sum/count)