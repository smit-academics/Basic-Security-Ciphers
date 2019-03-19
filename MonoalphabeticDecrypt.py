x = input("Enter Secret Message:").upper();
print(x)
k={}
kl=['B','C','M','K','Q','E','P','U','R','D','Z','V','F','X','G','H','J','I','W','O','T','L','A','S','Y','N']

for i in range(26):
	#k[chr(i+65)] = chr((i+10)%26+65)
	k[kl[i]] = chr(i+65)

#print(k['K'])

pt=[]
i = 0
for j in x:
	#print(j)
	#print(k[j])
	pt.append(k[j])
	i += 1

#print(pt)
print('Plain Text = ',end='')
for x in pt:
	print(x,end='')
