import random
def check(x):
	for i in x:
		for j in i:
			if j !=0:
				return True
	return False		
def find_vertex_cover(edges):
	c = set()
	e = edges
	while(check(e)):
		a = random.randrange(0,5,1)
		b = random.randrange(0,5,1)
		if e[a][b] !=0 :
			for i in range(0,5):
				e[a][i] = e[i][a] = e[b][i] = e[i][b] =0
			c.add(a)
			c.add(b)
		print(e)
		
		
	
	return c		

if __name__ == "__main__":
	edges=[[0,1,1,0,0],[1,0,0,1,1],[1,0,0,1,0],[0,1,1,0,0],[0,1,0,1,0]]
	answer = find_vertex_cover(edges)
	print(answer)
