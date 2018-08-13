print("This program is a conditional test.");

a=5;

print();print("Using | symbol");
if (a > 1) | (a < 10):
    print('condition is true');

print();print("Using or");
if (a > 1) or (a < 10):
    print('condition is true');

print();print("Elif and Else");
if a>10:
	print('Condition is true');
elif a>6:
	print('Second condition is true');
else:
	print('False condition');

print();print("Truthy and False");
a=0;
if a:
    print("Number tested is truthy");
else:
    print("Number is falsy");


print();print("Ternary If-Else Statement");
a=3;
b=5;
print("bigger" if a > b else "smaller");

print();print("Ternary if-else statement with and/or");
print("condition true" if a > 1 and a < 4 else "condition false");

print();print('Program Over');
