import random
print("Menampilkan Bilangan secara acak yang dibawah 0.5")
n = int(input("\nMasukkan Jumlah N : "))
a = 0
for x in range(0,n):
	i = random.uniform(.0,.5)
	a+=1
	print("Data ke-",a," :",i)
print("\nSelesai")