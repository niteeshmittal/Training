print("This program is to practice star programs.");

beg=1;
end=6;
for i in range(beg,end):
	for j in range(beg,i+1):
		print('*',end=' ');
	print();

print();print();

for i in reversed(range(beg,end)):
	for j in range(beg,i+1):
		print('*',end=' ');
	print();

print();print();

for i in range(beg,end):
	for j in range(beg,i+1):
		print('*',end=' ');
	print();
for k in range(j-1,0,-1):
	for m in range(beg,k+1):
		print('*',end=' ');
	print();

print();print();

for i in range(beg,end,1):
	for j in range(beg,i+1,1):
		print('*',end=' ');
	for k in range(8,2*(i-1),-1):
		print(' ',end=' ');
	for l in range(beg,i+1,1):
		print('*',end=' ');
	print();

print('Program Over');