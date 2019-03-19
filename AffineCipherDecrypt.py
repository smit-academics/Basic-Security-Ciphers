def gcd(a,b):
	if (b==0):
		return a
	else:
		return gcd(b,a%b)

#find Invertible numbers
nums = []
for k in range(26):
	if(gcd(26,k) == 1):
		#print(k)
		nums.append(k)
#print(nums)

#find Inverse Pairs
inv = []
for k in nums:
	for a in nums:
		if( ((a*k)%26 == 1) and a!=k ):
			#print((k,a))
			inv.append((k,a))

#---------Encryption----------
x = input("Enter Cipher Text:");
while(not x.isalpha()):
	print('invalid value')
	x = input("Enter Cipher Text:");
k1 = int(input("Enter Key 1:"))
while((int(k1) not in nums) or k1 == 1):
	print('Value is not invertible. Please try other')
	k1 = int(input("Enter Key 1:"))

#----set k1 as inverse of k1----
for k in inv:
	if( k[0] == k1):
		k1_inv = k[1]

#print(k1_inv)	

k2 = input("Enter Key 2:")
while(not k2.isdigit()):
	print('invalid value')
	k2 = input("Enter Key 2:")
k2 = int(k2)

x=x.upper()
ct = []
for i in x:
	#print(ord(i))
	ct.append(ord(i)-65)
#print(ct)

pt = [0 for y in range(len(ct))]

for i in range(len(ct)):
	pt[i] = (ct[i] - k2)%26

#print(pt)

for i in range(len(ct)):
	pt[i] = (pt[i]*k1_inv)%26

#print(pt)

print('Plain Text')
for a in pt:
	print(chr(a+65),end='')
