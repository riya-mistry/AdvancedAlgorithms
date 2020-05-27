import math
class convex:

	def __init__(self,x,y):
		self.x=x
		self.y=y
	

def select_origin(l):
	c=l[0]
	for i in range(1,len(l)):
		if c.y>l[i].y:
			c=l[i]
		elif c.y ==l[i].y:
			if c.x>l[i].x:
				c=l[i]
	return c
				
def choose_points(l,a):
	l1=[]
	for i in range(0,len(l)):
		demo=l[i]
		for j in range(i,len(l)):
			if a[i]==a[j]:
				if l[i].x<l[j].x and l[i].y<l[j].y:
					demo=l[j]
		l1.append(demo)
	l1=list(dict.fromkeys(l1))
	l1=sorted(l1, key=lambda convex: convex.y)
	l1=sorted(l1, key=lambda convex: convex.x)  
	return l1		

def find_Angle(l):	
	a=[]
	for i in l:
		a.append((math.atan2(i.y,i.x)*180)/math.pi)
	
	return a

def direction(p0,p1,p2):
	x=((p2.x-p0.x)*(p1.y-p0.y))-((p1.x-p0.x)*(p2.y-p0.y))
	return x
def grahamscan(points):
	answer=[]
	
	answer.append(points[0])
	answer.append(points[1])
	answer.append(points[2])
	for i in range(3,len(points)):
		while(direction(answer[-2],answer[-1],points[i])>=0):
			answer.pop()
			
		answer.append(points[i])
	print("points in polygon are:")
	for i in answer:
		print(i.x, i.y)		





if __name__=="__main__":
	points=[]
	angles=[]
	points.append(convex(0,0))
	points.append(convex(3,1))
	points.append(convex(1,1))
	points.append(convex(2,2))
	points.append(convex(3,3))
	points.append(convex(4,4))
	points.append(convex(1,2))
	points.append(convex(0,3))
	angles=find_Angle(points)
	c1=select_origin(points)
	filtered_points=choose_points(points,angles)
	print("points are")
	for i in filtered_points:
		print(i.x, i.y)
	grahamscan(filtered_points)
	
	
	
