import random
def check(x):
	for i in x:
		for j in i:
			if j !=0:
				return True
	return False	
def checkDegree(v,e):
	final = 0
	vertex = 0
	for i in v:
		count = sum(e[i])
		if final <= count:
			final = count
			vertex = i
	return vertex
def find_vertex_cover(edges):
	c = set()
	e = edges
	v = [0,1,2,3,4]
	while(check(e)):
		a = checkDegree(v,e)
		print(a)
		c.add(a)
		for i in range(0,5):
				e[a][i] = e[i][a] =0
		v.remove(a)
		
	
	return c		

if __name__ == "__main__":
	edges=[[0,1,1,0,0],[1,0,0,1,1],[1,0,0,1,0],[0,1,1,0,0],[0,1,0,1,0]]
	answer = find_vertex_cover(edges)
	print(answer)
