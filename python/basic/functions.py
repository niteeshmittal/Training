print('This program is to practice functions.');

#First basic functions
def hellofunction( str ):
	"This functions accepts a str and prints the same on console."
	print(str);
	return;
	
hellofunction("Hello, this is my first program def and call. Function doesn't return any value.");
hellofunction("This is second time I am calling same function which doesn't return any value.");

def sum(num1, num2):
	sum = num1 + num2;
	return sum;

total = sum(10,20);
print();print("Sum function which return the total of any two values passed, 10 and 20 in this case: ", total);

#Odd-even test
def oddeven(num):
	"Function to test even odd number."
	if(num%2==0):
		print('%d is an even number' % num);
	else:
		print('%d is an odd numner' % num);
	return;

print();print("Function to test even odd number.");
for i in range(1,11):
	oddeven(i);
	
#Pass by reference test
def refpasstest(num):
	"This function is to test the pass by reference value."
	num = num + 10; #It uses the passed value and add 10 in the that, then assigns the results to the local variable with the same name.
	print("Num variable value inside function: ",num);
	num = num + 10; #It will use the local variable value, add 10 in that and assigns the results to the local variable.
	print("Num variable value inside function: ",num);
	return;

num=4;
print();print("Num variable value before calling function: ", num);
refpasstest(num);
print("Num variable value after calling function: ", num);
del num;

#Variable length argument function
def varlenarg(num1, *num2, num3=35):
	"This function is to test variable lenth arguments."
	print();print("Function 1 outputs:");
	print("Num 2 is:",end=' ');
	for i in num2:
		print(i,end=' ');
	print();print("Num 1 is:",num1);
	print("Num 3 is:",num3);
	return;
	
varlenarg(50);			#this goes to num1 parameter of the function
varlenarg(10,20,40,50);	#10 goes to num1, rest values goes to num2 tuple

#Variable length argument function 2
def varlenarg1(num1, num3=35, *num2):
	"This function is to test variable lenth arguments."
	print();print("Function 2 outputs:");
	print("Num 2 is:",end=' ');
	for i in num2:
		print(i,end=' ');
	print();print("Num 1 is:",num1);
	print("Num 3 is:",num3);
	return;
	
varlenarg1(50);				#this goes to num1 parameter of the function
varlenarg1(10,20,40,50);	#10 goes to num1, 20 goes to num3 and rest values goes to num2 tuple

#Annonymous Function
asum = lambda num1, num2: num1 + num2;
print();print("A annonymous function sum to get the sum of 10 and 20: ",asum(10, 20));
print("Using same annonymous function sum to get the sum of 450 and 200: ",asum(450, 200));

#