def pay():
	days=45
	rate = 10
	x = days * rate
	return days
  
print("pay:",pay())

def computepay(hour, rate):
    pay = hour * rate
    return pay

xh = input("Enter Hours:")

xr = input("Enter Rate:")


try:
    fh = float(xh)
    fr = float(xr)

    print("Pay: ",computepay(fh,fr))
except:
    print("Error, please enter numeric input") 

 