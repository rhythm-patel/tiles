# Anuneet Anand [2018022]
# Rhythm Patel [2018083]
# EndSem Programming Assignment

import sys
import time
sys.setrecursionlimit(10000000)
starttime=time.time()
Answer = {}
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

def DFS(startNode,sink,visited=set(),curPath = []):
	# print ("Start:",startNode)
	visited.add(startNode)
	Bool = False
	curPath = curPath + [startNode] 

	if sink in Graph[startNode]: # if sink reachable
		curPath = curPath + [sink]
		paths.append(curPath)
		# print ("sink cond")
		return True

	for vertex in Graph[startNode]:
		if (vertex not in visited):
			# print ("vertex",vertex,',',startNode)
			Bool = DFS(vertex,sink,visited,curPath)
			if (Bool == True) and (startNode != 'S'):	
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
	sys.exit(0)
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
		Status = False
		paths = []
		Status = DFS("S","T",set())
		for p in paths:
			for i in range(len(p)-1):
				a=p[i]
				b=p[i+1]
				Graph[a].remove(b)
				Graph[b].append(a)
				Capacity[a,b]=0 #NOT REALLY IMP
				Capacity[b,a]=1
		# for k in Graph:
			# print (k,":",Graph[k])
		for p in paths:
			temp = p[::-1]
			temp = temp[1:-1]
			for i in range(0,len(temp)-1,2):
				Answer[temp[i]]=temp[i+1]
				Status = True
				# if temp[i+1] in Answer:
				# 	Answer[temp[i+1]]=temp[i]
				# else:
				# 	Answer[temp[i]]=temp[i+1]
		# print ("Status last: ", Status)
				
		# print(Answer)

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

	if len(Answer)!=len(A):
		print(0)
	else:
		print(1)
		for i in Answer:
			a = i[0]+1
			b = i[1]+1
			c = Answer[i][0]+1
			d = Answer[i][1]+1
			print( "(",a,",",b,")","(",c,",",d,")",sep="")
endtime=time.time()
print(endtime-starttime)




