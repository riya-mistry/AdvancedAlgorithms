def hp(t,p):
	table={}
	m=len(p)
	n=len(t)
	z=ord('A')
	for i in range(0,26):
		table[chr(z+i)]=m
		
	for j in range(0,m-1):
		table[p[j]]=m-1-j
	i=m-1
	while(i<=n-1):
		k=0
		while( k<m and p[m-1-k]==t[i-k]):
			k=k+1
		if k==m:
			return i-m+1
		else:
			if t[i] in table.keys():
				i=i+table[t[i]]
			else:
				i=i+m

if __name__=='__main__':
	text=raw_input()
	pattern=raw_input()
	s=hp(text,pattern)
	print('pattern match at shift:'+ str(s))
