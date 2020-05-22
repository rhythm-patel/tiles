# Anuneet Anand [2018022]
# Rhythm Patel [2018083]
# EndSem Programming Assignment

import time
import sys
sys.setrecursionlimit(10000000)
starttime=time.time()

def Check(n,r,c):
	if r>=0 and r<n and c>=0 and c<n:
		return True
	else:
		return False

# def DFS(s,V,P,G,C,F):
# 	V[s]=1
# 	for x in G[s]:
# 		if x not in V and C[(s,x)]>F[(s,x)]:
# 			V[x]=1
# 			P[x]=s
# 			if x == "T":
# 				return True
# 			if DFS(x,V,P,G,C,F):
# 				return True
# 	return False

# DFS("S",V,Parent,Graph,Capacity,Flow)

def DFS(start,end,visited=set(),path = []):
	Bool = False
	visited.add(start)
	path = path + [start] 

	if end in Graph[start]: # if end reachable
		path = path + [end]
		paths.append(path)
		return True

	for vertex in Graph[start]:
		if (vertex not in visited):
			Bool = DFS(vertex,end,visited,path)
			if (start != 'S') and Bool:	
				break

	return Bool



A = []
B = []

with open("input-1.txt","r") as InputFile:
	I = InputFile.readlines()
	n = int(I[0])
	Grid = [[0 for i in range(n)] for j in range(n)]
	for r in range(n):
		for c in range(n):
			Grid[r][c]=int(I[r+1][c])
			if Grid[r][c]==1:
				if (r+c)%2==0:
					A.append((r,c))
				else:
					B.append((r,c))

if (len(A)!=len(B)):
	print(0)
if len(A)==0:
	print(1)
else:
	Graph = {}
	Capacity = {}

	for a in A:
		Graph[a]=[]
	for b in B:
		Graph[b]=[]

	for i in range(len(A)):
		r,c = A[i][0],A[i][1]
		if Check(n,r+1,c):
			if Grid[r+1][c]==1:
				Graph[r,c].append((r+1,c))
				Capacity[((r,c),(r+1,c))]=1
				# Graph[r+1,c].append((r,c))
				# Capacity[((r+1,c),(r,c))]=0

		if Check(n,r,c+1):
			if Grid[r][c+1]==1:
				Graph[r,c].append((r,c+1))
				Capacity[((r,c),(r,c+1))]=1
				# Graph[r,c+1].append((r,c))
				# Capacity[((r,c+1),(r,c))]=0

		if Check(n,r-1,c):
			if Grid[r-1][c]==1:
				Graph[r,c].append((r-1,c))
				Capacity[((r,c),(r-1,c))]=1
				# Graph[r-1,c].append((r,c))
				# Capacity[((r-1,c),(r,c))]=0

		if Check(n,r,c-1):
			if Grid[r][c-1]==1:
				Graph[r,c].append((r,c-1))
				Capacity[((r,c),(r,c-1))]=1
				# Graph[r,c-1].append((r,c))
				# Capacity[((r,c-1),(r,c))]=0

	Flow = {}
	Graph["S"]=[]
	Graph["T"]=[]

	for x in A:
		Graph["S"].append(x)
		Capacity[("S",x)] = 1
	for y in B:
		Graph[y].append("T")
		Capacity[(y,"T")] = 1
	for z in Capacity:
		Flow[z]=0

	MaxFlow = 0
	print(time.time()-starttime)
	V={}
	Parent={}

	# setAVisited = []
	# for elem in A:
	# 	setAVisited.append(elem)

	# Status = DFS("S",V,Parent,Graph,Capacity,Flow)
	
	# print(Graph)
	# graph = {(0, 0): [(0, 1)], (2, 2): [(2, 1)], (0, 1): ['T'], (2, 1): ['T'], 'S': [(0, 0), (2, 2)], 'T': []}
	Status = True
	c=1
	while (Status == True):
		paths = []
		Status = DFS("S","T")
		for i in range(len(paths)-1)
			a=paths[i]
			b=paths[i+1]
			Graph[a].pop(b)
			Graph[b].append(a)
			Capacity[a,b]=0 #NOT REALLY IMP
			Capacity[b,a]=1
		print(paths)

	# while Status:
	# 	#f = 1
	# 	x = "T"
	# 	f =  1000000
	# 	while x!="S":
	# 		f = min(f,Capacity[(Parent[x],x)]-Flow[(Parent[x],x)])
	# 		x = Parent[x]
	# 	MaxFlow += f
	# 	x = "T"
	# 	while x!="S":
	# 		Flow[(Parent[x],x)] += f
	# 		if x!="T" and Parent[x]!="S":
	# 			Flow[(x,Parent[x])] -= f
	# 		x = Parent[x]
	# 	V={}
	# 	Parent={}
	# 	Status = DFS("S",V,Parent,Graph,Capacity,Flow)
	# 	# print(MaxFlow)

	# Answer = []
	# for x in Flow:
	# 	if Flow[x]>0 and "S" not in x and "T" not in x :
	# 		a,b = list(x[0]),list(x[1])
	# 		a[0]+=1
	# 		a[1]+=1
	# 		b[0]+=1
	# 		b[1]+=1
	# 		Answer.append([tuple(a),tuple(b)])

	# if len(Answer)!=len(A):
	# 	print(0)
	# else:
	# 	print(1)
	# 	for i in Answer:
	# 		a = i[0]
	# 		b = i[1]
	# 		print( "(",a[0],",",a[1],")","(",b[0],",",b[1],")",sep="")
endtime=time.time()
print(endtime-starttime)




