# Anuneet Anand [2018022]
# Rhythm Patel [2018083]
# EndSem Programming Assignment

import sys
import time
sys.setrecursionlimit(1000000)							# Please change depending on system

Start_Time=time.time()

Solvable = 0												
Graph = {}														
Answer = {}
A = []
B = []

def Check(n,r,c):										# To check for valid cell in Grid
	if r>=0 and r<n and c>=0 and c<n:
		return True
	else:
		return False

def DFS(S,T,Visited=set(),Path = []):					# TP find all valid paths from S to T
	Visited.add(S)
	Flag = False
	Path = Path + [S] 

	if T in Graph[S]:
		Path = Path + [T]
		All_Paths.append(Path)
		return True

	for V in Graph[S]:
		if (V not in Visited):
			Flag = DFS(V,T,Visited,Path)
			if (Flag) and (S != 'S'):	
				break
	return Flag

with open("input.txt","r") as InputFile:				# Reading input from file
	I = InputFile.readlines()
	n = int(I[0])
	Grid = [[0 for i in range(n)] for j in range(n)]
	for r in range(n):
		for c in range(n):
			Grid[r][c]=int(I[r+1][c])
			if Grid[r][c]==1:							# Alloting elements to set A & set B
				if (r+c)%2==0:
					A.append((r,c))
				else:
					B.append((r,c))

if (len(A)!=len(B)):									# Can't be tiled
	Solvable = 0
elif len(A)==0:
	Solvable = 1										# Already tiled
else:

	for a in A:
		Graph[a]=[]
	for b in B:
		Graph[b]=[]

	Graph["S"]=[]										# Source
	Graph["T"]=[]										# Sink

	for i in range(len(A)):								# Constructing Graph
		r,c = A[i][0],A[i][1]
		if Check(n,r+1,c):								# Bottom Cell
			if Grid[r+1][c]==1:
				Graph[r,c].append((r+1,c))

		if Check(n,r,c+1):								# Right Cell
			if Grid[r][c+1]==1:
				Graph[r,c].append((r,c+1))

		if Check(n,r-1,c):								# Top Cell
			if Grid[r-1][c]==1:
				Graph[r,c].append((r-1,c))

		if Check(n,r,c-1):								# Left Cell
			if Grid[r][c-1]==1:
				Graph[r,c].append((r,c-1))

	for x in A:
		Graph["S"].append(x)
	for y in B:
		Graph[y].append("T")

	Status = True
	while Status:
		Status = False
		All_Paths = []
		Status = DFS("S","T",set())
		for Path in All_Paths:
			for i in range(len(Path)-1):				# Reversing Used Edges
				a=Path[i]
				b=Path[i+1]
				Graph[a].remove(b)
				Graph[b].append(a)

		for Path in All_Paths:							# Updating Parents
			Rev = Path[::-1]
			Rev = Rev[1:-1]
			for i in range(0,len(Rev)-1,2):
				Answer[Rev[i]]=Rev[i+1]
				Status = True

	if len(Answer)!=len(A):								# All Cells can't be tiled
		Solvable = 0
	else:
		Solvable = 1


with open("output.txt","w") as OutputFile:				# Writing output to file
	if Solvable == 1:
		OutputFile.write("1"+"\n")
		for x in Answer:
			a = x[0]+1
			b = x[1]+1
			c = Answer[x][0]+1
			d = Answer[x][1]+1
			Output = "("+str(a)+","+str(b)+")"+"("+str(c)+","+str(d)+")"+"\n"
			OutputFile.write(Output)
			#print( "(",a,",",b,")","(",c,",",d,")",sep="")
	else:
		OutputFile.write("0"+"\n")

End_Time=time.time()
print("Execution Time:",End_Time-Start_Time)			# Timing Code

# END OF CODE