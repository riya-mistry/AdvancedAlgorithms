import random
count=0
def quicksort(A,p,r):
	
	if p < r:
		q = partition(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q,r)
		
		
def partition(A,p,r):
	global count
	index = (random.randrange(p,r+1))
	A[index] , A[r] = A[r],A[index]
	
	x = A[r]
	i = p-1

	for j in range(p,r):
		if A[j] <= x :
			count+=1
			i += 1
			A[i],A[j] = A[j],A[i]
	A[i+1],A[r]  = A[r] , A[i+1]
	
	return i+1
	




if __name__ == "__main__":
	array = []
	for i in range(1000):
		array.append(i)
	quicksort(array,0,len(array)-1)
	print("comparisons are " + str(count))
	#print(array)
