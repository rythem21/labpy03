max = 0
while True:
	b = int(input("Masukkan bilangan : "))
	if(max<b):
		max = b
	elif(b == 0):
		break
print("\nBilangan Terbesar adalah",max)