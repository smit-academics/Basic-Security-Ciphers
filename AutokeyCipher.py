x = input("Enter Secret Message:").upper();

k1 = input("Enter k1:");
while(not k1.isdigit()):
	print('Invalid Number');
	k1 = input("Enter k1:");

#print(k1)
k = [int(k1)]

for i in x:
	k.append(ord(i)-65)
	#print(ord(i)-65)
	
print(k)

ct = []

for i in range(len(x)):
	num = ((ord(x[i])-65) + k[i])%26
	ct.append( chr(num + 65) ) 

for x in ct:
	print(x,end='')
