'''
	some cases are missing in last loop

'''

x = input("Enter Secret Message :").upper();
k=input('enter key :').upper()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(alpha)):
	alpha[i] = alpha[i].upper()


kMat = []

t=0;
for i in range(5):
	kMat.append([])
	for j in range(5):
		while( (len(k) > t) and (not alpha.count(k[t])>0)):
			t += 1
		
		if(len(k) > t):
			#print('k=',k[i], 'i=',i, 'j=', j )
			kMat[i].append(k[t])
			alpha.remove(k[t])
		else:
			if(alpha[0] == 'i'):
				if(alpha.count('j')>0):
					alpha.remove('j')
				else:
					alpha.remove(alpha[0])
				
			kMat[i].append(alpha[0])
			alpha.remove(alpha[0])
			
		t += 1
#print(alpha)
print()
for i in range(5):
	print(kMat[i])

a=0
b=0
ct=[]
for i in range(0,len(x),2):
	if(i+1 < len(x)):
		
		if(x[i] == x[i+1]):
			#x.insert(i+1,'x')
			x = x[:i+1] + 'X' + x[i+1:]
		for p in range(5):
			for q in range(5):
				#print('kmat = ',kMat[p][q],'xi=',x[i])
				if(kMat[p][q] == x[i]):
					a = kMat[p][q]
					ai = (p,q)
				if(kMat[p][q] == x[i+1]):
					b = kMat[p][q]
					bi = (p,q)

		print(x[i],x[i+1],end=' : ')
		#print(a,ai,b,bi)
		print(kMat[ai[0]][bi[1]],end=' ')
		print(kMat[bi[0]][ai[1]])
		ct.append(kMat[ai[0]][bi[1]])
		ct.append(kMat[bi[0]][ai[1]])
	else:
		print(x[i])

print(ct)
