x = input("Enter Secret Message:").upper();

k=[]
i = 0
t = input('Enter Key digits (enter non-digit value to finish):')
while(t.isdigit()):
	k.append(int(t)%26)
	t = input()
	i += 1

print('Key entered is ',k)

while(len(k) < len(x)):
	k.extend(k)

k = k[:len(x)]
print('final key:',k[:len(x)])
#print(x)


ct = []
for i in range(len(x)):
	num = ((ord(x[i])-65) + int(k[i]))%26
	ct.append( chr(num + 65) ) 

for x in ct:
	print(x,end='')

