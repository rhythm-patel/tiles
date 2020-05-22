n = 250
f = open("input-4.txt","w")
f.write("250\n")
for i in range(n):
	for j in range(n):
		f.write("1")
	f.write("\n")
f.close()