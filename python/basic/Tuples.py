print("This program is to practice Tuples.");

#Creating Tuples
#Empty tuple
etup=();
print();print('Empty Tuple: ',etup);

#Single Value Tuple without comma
sttup=(50);
print();print('single Value Tuple without comma, which is treated as integer variable: ',sttup); #this will treat sttup as integer variable not a tuple

#Single Value Tuple with comma
stup=(50,);
print();print('Proper single Value Tuple: ',stup);

#Multi Value Tuple with comma
num_tup=(1,3,5,2,7,88,9);
print();print('Multivalue number only tuple: ',num_tup);

#Multi Value Tuple with comma
str_tup=('Books','Travel','Movies','Games');
print();print('Multivalue number only tuple: ',str_tup);

#Access only specific value from any tuple
print();print('Second value from number tuple: ', num_tup[1]);

#Try to modify a tuple
#num_tup[1]=99; #This throws an error because tuples are immutable, to test, remove # symbol from the beginning of the line.

#Creating a tuple without parenthesis
new_tup=50,'Game',78,'Books';
print();print('Tuple created without specifying parenthesis: ',new_tup);

print('Program Over');