x = input("Enter Cipher:").upper();

k1 = input("Enter k1:");
while(not k1.isdigit()):
	print('Invalid Number');
	k1 = input("Enter k1:");
k1=int(k1)
#print(k1)
k = [int(k1)]

print( (ord(x[0])-65 - k1)%26);

pt=[]
for i in range(len(x)):
	kk = (ord(x[i])-65 - k[i])%26
	#print(kk);
	k.append(kk)
	pt.append(kk)

#print(pt)
for x in pt:
	print(chr(x+65),end='')
