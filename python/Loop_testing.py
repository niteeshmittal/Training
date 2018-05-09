print("This program is a Loop test.");

print("While Loop")
count=0;
while (count<5):
	print(count,' is less than 5');
	count+=1;
else:
	print(count,' is not less than 5');

print('For Loop with else')
for num in range(1,11):
	print('Number is: ',num);
else:
	print('Loop end. Now the number is: ',num);

print('Loop with only end value');
for num in range(10):
	print(num,end=' ');

print();print('For Loop by Step method');
for num in range(1,11,2):
	print(num,end=' ');

print();print('Reveresed Loop with only end value');
for num in reversed(range(10)):
	print(num,end=' ');

print();print('Reversed loop with both start and end value');
for num in reversed(range(1,11)):
	print(num,end=' ');

print();print('Reverse loop by step method');
for num in range(10,0,-1):
	print(num,end=' ');

print();print('Pass Statement');
for num in range(10,0,-1):
	if (num==5):
		pass;
	print(num,end=' ');

print();print('Break Statement');
for num in range(10,0,-1):
	if (num==5):
		break;
	print(num,end=' ');

print();print('Continue Statement');
for num in range(10,0,-1):
	if (num==5):
		continue;
	print(num,end=' ');

print();print('Program Over');