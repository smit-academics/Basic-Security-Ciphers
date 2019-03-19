def gcd(a,b):
	if (b==0):
		return a
	else:
		return gcd(b,a%b)

nums = []
for k in range(26):
	if(gcd(26,k) == 1):
		#print(k)
		nums.append(k)
'''
print(nums)
for k in nums:
	for a in nums:
		if( ((a*k)%26 == 1) and a!=k ):
			print((k,a))
			pass
'''

#---------Encryption----------
# take inputs and validate them
x = input("Enter Secret Message:");
while(not x.isalpha()):
	print('invalid value')
	x = input("Enter Secret Message:");
k1 = int(input("Enter Key 1:"))
while((int(k1) not in nums) or k1 == 1):
	print('Value is not invertible. Please try other')
	k1 = int(input("Enter Key 1:"))
k2 = input("Enter Key 2:")
while(not k2.isdigit()):
	print('invalid value')
	k2 = input("Enter Key 2:")
k2 = int(k2)

#represent plaintext
x=x.upper()
pt = []
for i in x:
	#print(ord(i))
	pt.append(ord(i)-65)
#print(pt)

ct = [0 for y in range(len(pt))]
for i in range(len(pt)):
	ct[i] = (pt[i]*k1)%26

#print('after multiplication k is')
#print(ct)

for i in range(len(pt)):
	ct[i] = (ct[i] + k2)%26

print('Cipher Text')
for a in ct:
	print(chr(a+65),end='')

