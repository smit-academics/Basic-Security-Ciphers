x = input("Enter Secret Message:");
k = int(input("Enter Key:"))


p = ''
for i in x:
	if(ord(i)<97 or ord(i)>122):
		print('Wrong Input Encountered. Please Enter Small Alphabets only')
		exit(0)
	p += chr( ((ord(i)-97+k) %26)+97 ) 

print(p)
